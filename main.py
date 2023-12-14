from aria2 import download_manager, is_valid_url
from Youtube import download_video
from soundcloud import soundcloud
from Light_novels import download_novel
from sources import sources
from spotifiy import spotify
from edit_video import *
from wallfetch import download_wallpapers
from Upload import Upload
from gimages import download_gimages
from photos import download_photos
from FFMPEG import ffmpeg_install

import time
import os
import gdown

subprocess.run(["pip", "install", "-r", "requirements.txt"])
ffmpeg_install()

while True:
    os.system("cls")

    choice = input(
        '''1-Download Manager      2-Youtube Downloader      3-Soundcloud Downloader      4-Lightnovels Downloader      5-Spotify Downloader \n6-Video Editing         7-Download Wallpapers     8-Google Drive Downlaod      9-Upload file                 10-Download Photos  \n11-Download Gimages     12-Quit\n'''
    )

    if (choice == "1"):
        download_manager()
    elif (choice == "2"):
        os.system("cls")
        URL = input("Enter the link of the video/playlist: ")
        QUALITY = input(
            "Enter the quality (144p,240p,480p,720p,1080p,2K,4K,8K): ")
        download_video(URL, QUALITY)
        time.sleep(3)
        os.system("cls")
        print("Download Finished")
        time.sleep(3)

    elif (choice == "3"):
        URL = input("Enter a URL for a track/playlist/user: ")
        if (is_valid_url(URL)):
            soundcloud(URL)
            time.sleep(3)
            os.system("cls")

        else:
            print("Wrong URL entered..")
            time.sleep(2)

    elif (choice == "4"):
        os.system("cls")
        x = input("1-Show Sources   2-Enter Link to download\n")
        if (x == "1"):
            for i, source in enumerate(sources.items(), start=1):
                print(f"{i}. {source[1]['name']} {source[1]['link']}")

            input('Enter anything to go back!')
            os.system("cls")

        elif (x == "2"):
            URL = input("Enter the URL: ")
            if (is_valid_url(URL)):
                Rng = input(
                    "Enter the range in this format (start end) or type all: ")
                download_novel(URL, Rng)
                os.system("cls")
                print("Novel Downloaded Successfully!")
                time.sleep(2)
            else:
                print("Wrong URL entered..")
                time.sleep(2)

    elif (choice == "5"):
        os.system("cls")
        URL = input("Enter the URL of the song: ")
        if (is_valid_url(URL)):
            spotify(URL)
            print("Donwload finished")
            time.sleep(2)
            os.system("cls")
        else:
            print("Wrong URL entered..")
            time.sleep(2)

    elif (choice == "6"):
        x = input(
            "1-Convert Video    2-Compress Video CPU (slow but smaller and better quality)   3-Compress Video GPU (faster but bigger size and lower quality)\n"
        )

        if (x == "1"):
            path = input("Enter the video path: ")
            ext = input("Enter the extension you want: ")
            convert_video(path, ext)
            print("Done converting!")
            time.sleep(2)

        elif (x == "2"):
            path = input("Enter the video path: ")
            CRF = input(
                "Enter the qulity factor(0-51) the lower the higher the qulity but the bigger the size (Ideal 28~32): "
            )
            compress_video(path, CRF)
            print("Done compressing!")
            time.sleep(2)

        elif (x == "3"):
            path = input("Enter the video path: ")
            CRF = input(
                "Enter the qulity factor(0-51) the lower the higher the qulity but the bigger the size (Ideal 28~32): "
            )
            compress_video_GPU(path, CRF)
            print("Done compressing!")
            time.sleep(2)

        else:
            print("Wrong choice!")
            time.sleep(1)

    elif (choice == "7"):
        query = input("Enter the search query: ")

        number = int(
            input("Enter the number of images or enter 0 to cancel: "))
        if (number != 0):
            download_wallpapers(query, number)
            print("Download finished!")
            time.sleep(1.5)

    elif (choice == "8"):
        if not os.path.exists(
                os.path.join(os.getcwd(), 'GoogleDrive_Downloads/')):
            os.makedirs(os.path.join(os.getcwd(), 'GoogleDrive_Downloads/'))

        os.system("cls")
        x = input("1-Download a file      2-Download a folder\n")
        if (x == "1"):
            URL = input("Enter the file URL: ")
            if (is_valid_url(URL)):
                gdown.download(URL,
                               output=os.path.join(os.getcwd(),
                                                   'GoogleDrive_Downloads/'),
                               fuzzy=True)
                print("\n\nDownload Finished")
                time.sleep(2)

            else:
                print("wrong URL..")
                time.sleep(1.5)

        elif (x == "2"):
            URL = input("Enter the folder URL(maximum 50 files per folder): ")
            if (is_valid_url(URL)):
                gdown.download_folder(URL,
                                      output=os.path.join(
                                          os.getcwd(),
                                          'GoogleDrive_Downloads/'),
                                      quiet=False,
                                      use_cookies=False)
                print("\n\nDownload Finished")
                time.sleep(2)

            else:
                print("wrong URL..")
                time.sleep(1.5)

        else:
            print("Wrong choice...")
            time.sleep(1.5)

    elif (choice == "9"):
        path = input("Enter the the path to the file to upload\n")
        Upload(path)
        print("\n\nFinished Uploading!")
        input("Enter anyting to continue")

    elif (choice == "10"):
        url = input(
            "Enter the URL of the website you want to download photos from: ")
        if (is_valid_url(url)):
            download_photos(url)
            print("Download Finished")

        else:
            print("Bad URL")
        time.sleep(2)

    elif (choice == "11"):
        name = input("Enter the name of the photos you looking for: ")
        num = int(input("Enter the number of photos you want to download"))
        download_gimages(name, num)
        print("Download Finished")
        time.sleep(5)

    elif (choice == "12"):
        os.system("cls")
        quit()
    else:
        print("Wrong choice...")
        time.sleep(1)
        os.system("cls")
