# Import necessary libraries
import subprocess
import time
import os

# Install requirements from requirements.txt
subprocess.run(["pip", "install", "-r", "requirements.txt"])

from FFMPEG import ffmpeg_install
# Install FFMPEG
ffmpeg_install()

#import functions needed
from main_functions import *

# Define constants
MENU_OPTIONS = {
    "1": ("Download Manager", download_manager),
    "2": ("Youtube Downloader", download_youtube),
    "3": ("Soundcloud Downloader", download_soundcloud),
    "4": ("Lightnovels Downloader", download_lightnovels),
    "5": ("Spotify Downloader", download_spotify),
    "6": ("Video Editing", video_editing),
    "7": ("Download Wallpapers", download_wallpapers),
    "8": ("Google Drive Download", google_drive_download),
    "9": ("Download Photos", download_photos),
    "10": ("Download Gimages", download_gimages),
    "11": ("Quit", quit),
}


def prompt_user(message):
    return input(message)


def handle_invalid_choice():
    print("Wrong choice... Please try again.")
    time.sleep(1)
    os.system("cls")


def handle_operation(option):
    title, func = MENU_OPTIONS.get(option, (None, None))
    if title is not None:
        print(title)
        func()
    else:
        handle_invalid_choice()


# Main loop for the menu
while True:
    os.system("cls")  # Clear console

    # Print menu options
    for key, value in MENU_OPTIONS.items():
        print(f"{key}: {value[0]}")

    # Prompt user to choose an option
    choice = prompt_user("Enter your choice: ")

    # Handle user's choice
    handle_operation(choice)
