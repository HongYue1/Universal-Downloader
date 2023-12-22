import os
import time
import msvcrt

from colorama import init, Fore, Back, Style
from aria2_functions import *

init()


def download_manager():
    while True:
        os.system("cls")

        # Try to flush the buffer
        while msvcrt.kbhit():
            msvcrt.getch()

        choice = input(
            '''1-Add Download  2-Pause Download   3-Resume Download   4-Remove Download   5-Show Queue   6-Schedule link   7-Quit \n'''
        )

        os.system('cls')

        if choice == "1":
            add_download()
        elif choice == "2":
            pause_download()
        elif choice == "3":
            resume_download()
        elif choice == "4":
            remove_download()
        elif choice == "5":
            show_queue()
        elif choice == "6":
            schedule_link()
        elif choice == "7":
            break
        else:
            print(Fore.RED + "Wrong choice..." + Style.RESET_ALL)
            time.sleep(0.7)
