'''

Disabled for now, since Libtorrent doesn't work on windows


'''

import time
import libtorrent as lt
import os
from tqdm import tqdm

from threading import Thread

# Check if the download directory exists and create it if it doesn't
cwd = os.getcwd()
relative_path = 'Torrent_Downloads/'
download_directory = os.path.join(cwd, relative_path)
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Server Start
ses = lt.session()
ses.listen_on(6881, 6891)

# Torrent States
state_str = [
    "queued",
    "checking",
    "downloading metadata",
    "downloading",
    "finished",
    "seeding",
    "allocating",
    "checking fastresume",
]

downloads = []


# Add Torrent
def add_torrent():
    params = {"save_path": download_directory}
    link = input("Enter Magnet Link or Torrent File URL: ")
    downloads.append(lt.add_magnet_uri(ses, link, params))


# Remove Torrent
def remove_torrent():
    i = int(input("Enter your Choice : "))
    i -= 1

    for index, download in enumerate(downloads[:]):
        if (index == i):
            ses.remove_torrent(download)
            downloads.remove(download)
            print(download.name(), "Removed")
            break
    else:
        print("Torrent not found")
    time.sleep(2.5)


# This function calculates the speed of the download in a human-readable format
def rate(val):
    # List of prefixes for the units of speed
    prefix = ['B', 'kB', 'MB', 'GB', 'TB']
    # Loop through the prefixes
    for i in range(len(prefix)):
        # If the absolute value of the speed is less than 1000
        if abs(val) < 1000:
            # If the prefix is 'B', return the speed with 5 decimal places
            if i == 0:
                return '%5.3g %s' % (val, prefix[i])
            # Otherwise, return the speed with 4 decimal places
            else:
                return '%4.3g %s' % (val, prefix[i])
        # Divide the speed by 1000 to get the next unit
        val /= 1000

    # If the speed is still more than 1000, return the speed in 'PB' with 3 decimal places
    return '%6.3g PB' % val


class output:

    def __init__(self):
        self._running = True

    # Thread Killing
    def kill(self):
        self._running = False

    # Print Status Bar
    def show(self):
        while self._running:
            for index, download in enumerate(downloads[:]):
                s = download.status()
                print(
                    "No Torrent Name.   D.Speed U.Speed Downloaded Status  Progress"
                )
                print(" ".join([
                    str(index + 1) + ". \t",
                    download.name()[:25] + "...\t|\t",
                    '%s/s | ' % rate(s.download_rate),
                    '%s/s | ' % rate(s.upload_rate),
                    '%s Done | ' % rate(s.total_done),
                    state_str[s.state],
                ]))
                with tqdm(total=100,
                          ncols=50,
                          bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}',
                          position=index) as pbar:
                    pbar.update(s.progress * 100)
            #time.sleep(1)


def main():
    if downloads == []:
        print("No Torrent Found, Please add one")
        add_torrent()

    while True:
        os.system("cls")
        print(
            "No  Torrent Name.    D.Speed U.Speed Downloaded  Status   Progress"
        )

        bar = output()
        printing = Thread(target=bar.show)
        printing.start()

        time.sleep(2)

        print("[A] Add Torrent \t\t [R] Remove Torrent \t\t [Q] Quit")
        choice = input("Enter Choice : ")

        if choice.lower() == 'a':
            bar.kill()
            add_torrent()

        elif choice.lower() == 'r':
            bar.kill()
            remove_torrent()

        elif choice.lower() == 'q':
            bar.kill()
            print("Daemon Still Running")
            return

        else:
            bar.kill()
            print("Wrong Choice")


if __name__ == "__main__":
    main()
