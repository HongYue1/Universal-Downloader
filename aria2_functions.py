import re
import aria2p
import schedule
import keyboard
import os
import time
import threading

from start_aria import run_aria2

# Run the Aria2 downloader in the background
run_aria2()

# Initialize the aria2p client
aria2 = aria2p.API(aria2p.Client(host="http://localhost", port=6800,
                                 secret=""))

# Define constants
DOWNLOAD_DIRECTORY = 'Aria2_Downloads/'

# Check if the download directory exists and create it if it doesn't
cwd = os.getcwd()
download_directory = os.path.join(cwd, DOWNLOAD_DIRECTORY)
if not os.path.exists(download_directory):
    os.makedirs(download_directory)


def is_valid_url(url):
    # Regular expression pattern for URL validation
    pattern = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(pattern.match(url))


def convert_speed(speed_bytes_per_second):
    # Convert bytes/second to KB/s
    speed_KB_per_second = speed_bytes_per_second / 1024

    # If speed is equal to or higher than 1024KB/s, convert to MB/s
    if speed_KB_per_second >= 1024:
        speed_MB_per_second = speed_KB_per_second / 1024
        return str(round(speed_MB_per_second, 2)) + 'MB/s'
    else:
        return str(round(speed_KB_per_second, 2)) + ' KB/s'


def convert_size(size_in_bytes):
    size_in_kilobytes = size_in_bytes / 1024
    if (size_in_kilobytes < 1024):
        return str(round(size_in_kilobytes, 2)) + "KB"
    elif (size_in_kilobytes / 1024 < 1024):
        return str(round(size_in_kilobytes / 1024, 2)) + "MB"
    else:
        return str(round(size_in_kilobytes / (1024**2), 2)) + "GB"


def print_downloads():
    downloads = aria2.get_downloads()
    for index, download in enumerate(downloads, start=1):
        print(
            f"{index}. {download.name}, {convert_speed(download.download_speed)} , {convert_size(download.completed_length)} of {convert_size(download.total_length)}"
        )


def print_queue(stop_event):
    while not stop_event.is_set():
        print("Enter any key to go back: \n\nCurrent Queue: ")
        print_downloads()
        time.sleep(1)
        os.system("cls")


def get_input(stop_event):

    def on_press(event):
        stop_event.set()  # Set the flag to stop the threads
        print("Going back..")
        time.sleep(1.2)
        keyboard.unhook_all()  # Stop the listener

    keyboard.on_press(on_press)


def add_link(URL):
    print("Scheduled link started")
    aria2.add(URL, options={'dir': download_directory})
    return schedule.CancelJob


def run_schedule(link, time):
    schedule.every().day.at(time).do(add_link, link)
    while True:
        schedule.run_pending()
        time.sleep(1)


def add_download():
    URL = input("Enter the URL or enter any character to cancel: ")
    if is_valid_url(URL):
        aria2.add(URL, options={'dir': download_directory})
        print("Link added")
    else:
        print("Invalid URL or Going back...")
    time.sleep(1)
    os.system('cls')


def pause_download():
    print_downloads()
    all = input("\n1- Pause all  2- Selective pause. 3- Go back\n")
    if all == "2":
        selective_pause()
    elif all == "1":
        aria2.pause_all()
        print("All links paused")
    elif all == "3":
        return
    else:
        print("Wrong choice")

    time.sleep(1)
    os.system('cls')


def selective_pause():
    downloads = aria2.get_downloads()
    to_pause = []
    while True:
        download_number = int(
            input("Enter the files number to pause or 0 to stop: "))
        if download_number == 0:
            break
        try:
            to_pause.append(downloads[download_number - 1])
        except IndexError:
            print("Invalid download number.")
    aria2.pause(to_pause)
    print("Links paused")
    return


def resume_download():
    print_downloads()
    all = input("1- Resume all  2- Selective resume. 3- Go back\n")
    if all == "2":
        selective_resume()
    elif all == "1":
        aria2.resume_all()
        print("All links resumed")
    elif all == "3":
        return
    else:
        print("Wrong choice")

    time.sleep(1)
    os.system('cls')


def selective_resume():
    downloads = aria2.get_downloads()
    to_resume = []
    while True:
        download_number = int(
            input("Enter the files number to resume or 0 to stop: "))
        if download_number == 0:
            break
        try:
            to_resume.append(downloads[download_number - 1])
        except IndexError:
            print("Invalid download number.")
    aria2.resume(to_resume)
    print("Links resumed")
    return


def remove_download():
    print_downloads()
    all = input("1- Remove all  2- Selective remove. 3- Go back\n")
    if all == "2":
        selective_remove()
    elif all == "1":
        pathes = []
        downloads = aria2.get_downloads()
        for download in downloads:
            pathes.append(download.root_files_paths[0])
        aria2.remove_all()
        for i in pathes:
            os.remove(i)
        print("All links removed")
    elif all == "3":
        return
    else:
        print("Wrong Choice")

    time.sleep(1)
    os.system('cls')


def selective_remove():
    downloads = aria2.get_downloads()
    to_delete = []
    paths = []
    while True:
        download_number = int(
            input("Enter the files number to remove or 0 to stop: "))
        if download_number == 0:
            break
        try:
            to_delete.append(downloads[download_number - 1])
            paths.append(downloads[download_number - 1].root_files_paths)
        except IndexError:
            print("Invalid download number.")
    aria2.remove(to_delete)
    for i in paths:
        os.remove(str(i[0]))
    print("Links removed")
    return


def show_queue():
    aria2.purge()
    # Create an Event object
    stop_event = threading.Event()
    # Start the threads
    thread1 = threading.Thread(target=print_queue, args=(stop_event, ))
    thread2 = threading.Thread(target=get_input, args=(stop_event, ))
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()
    os.system('cls')


def schedule_link():
    link = input("Enter The link: ")
    time = input("Enter the time in the format (HH:MM): ")
    threading.Thread(target=run_schedule, args=(link, time)).start()
    print("Done!")
