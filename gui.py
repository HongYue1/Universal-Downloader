from tkinter import *
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

import time
import os
import gdown


def menu():
    unvirsal_downloader.destroy()
    global main_menu
    main_menu = Tk()
    main_menu.title("universal downloader")
    main_menu.config(bg="#2e3440")
    main_menu.geometry("1800x700")
    choose_label = Label(main_menu,
                         text="Choose To Start",
                         font="Georgia 25 italic bold",
                         fg="#7e8987",
                         bg="#2e3440")
    choose_label.grid(row=0, column=1, padx=30, pady=30)
    download_manager_button = Button(main_menu,
                                     text="Download Manager",
                                     bg="#7e8987",
                                     font="Georgia 25 italic bold",
                                     fg="#f0ebf5",
                                     width=20)
    download_manager_button.grid(row=1, column=0, padx=10, pady=30)
    youtube_downloader_button = Button(main_menu,
                                       text="YouTube Downloader",
                                       bg="#7e8987",
                                       font="Georgia 25 italic bold",
                                       fg="#f0ebf5",
                                       width=20,
                                       command=youtube_downloader)
    youtube_downloader_button.grid(row=1, column=1, padx=10, pady=30)
    soundcloud_downloader_button = Button(main_menu,
                                          text="SoundCloud Downloader",
                                          bg="#7e8987",
                                          font="Georgia 25 italic bold",
                                          fg="#f0ebf5",
                                          width=20,
                                          command=soundcloud_download)
    soundcloud_downloader_button.grid(row=1, column=2, padx=10, pady=30)
    lightnovels_downloader_button = Button(main_menu,
                                           text="LightNovels Downloader",
                                           bg="#7e8987",
                                           font="Georgia 25 italic bold",
                                           fg="#f0ebf5",
                                           width=20)
    lightnovels_downloader_button.grid(row=2, column=0, padx=10, pady=30)
    spotify_downloader_button = Button(main_menu,
                                       text="Spotify Downloader",
                                       bg="#7e8987",
                                       font="Georgia 25 italic bold",
                                       fg="#f0ebf5",
                                       width=20,
                                       command=soptify_download)
    spotify_downloader_button.grid(row=2, column=1, padx=10, pady=30)
    video_editing_button = Button(main_menu,
                                  text="Video Editing",
                                  bg="#7e8987",
                                  font="Georgia 25 italic bold",
                                  fg="#f0ebf5",
                                  width=20)
    video_editing_button.grid(row=2, column=2, padx=10, pady=30)
    download_wallpapers_button = Button(main_menu,
                                        text="Download Wallpapers",
                                        bg="#7e8987",
                                        font="Georgia 25 italic bold",
                                        fg="#f0ebf5",
                                        width=20,
                                        command=download_for_wallpaper)
    download_wallpapers_button.grid(row=3, column=0, padx=10, pady=30)
    googleDrive_download_button = Button(main_menu,
                                         text="Google Drive Download",
                                         bg="#7e8987",
                                         font="Georgia 25 italic bold",
                                         fg="#f0ebf5",
                                         width=20)
    googleDrive_download_button.grid(row=3, column=1, padx=10, pady=30)
    upload_file_button = Button(main_menu,
                                text="Upload File",
                                bg="#7e8987",
                                font="Georgia 25 italic bold",
                                fg="#f0ebf5",
                                width=20)
    upload_file_button.grid(row=3, column=2, padx=10, pady=30)
    quit_button = Button(main_menu,
                         text="Quit",
                         bg="#7e8987",
                         font="Georgia 25 italic bold",
                         fg="#f0ebf5",
                         command=exit)
    quit_button.grid(row=main_menu.grid_size()[1],
                     column=main_menu.grid_size()[0])
    main_menu.mainloop()


def youtube_downloader():

    youtube = Tk()
    youtube.title("universal downloader")
    youtube.config(bg="#2e3440")
    youtube.geometry("1800x700")
    youtube_label1 = Label(youtube,
                           text="enter the url of the playlist",
                           font="Georgia 25 italic bold",
                           fg="#7e8987",
                           bg="#2e3440")
    youtube_label1.grid(row=0, column=0, padx=30, pady=30)
    global youtube_url_textbox1
    global youtube_url_textbox2
    youtube_url_textbox1 = Entry(youtube, width=70)
    youtube_url_textbox1.grid(row=0, column=1, padx=30, pady=30)
    youtube_label2 = Label(
        youtube,
        text="enter the quality you want (144p,240p,480p,720p,1080p)",
        font="Georgia 25 italic bold",
        fg="#7e8987",
        bg="#2e3440")
    youtube_label2.grid(row=1, column=0, padx=30, pady=30)
    youtube_url_textbox2 = Entry(youtube, width=70)
    youtube_url_textbox2.grid(row=1, column=1, padx=30, pady=30)
    youtube_download_button = Button(youtube,
                                     text="Download",
                                     bg="#7e8987",
                                     font="Georgia 45 italic bold",
                                     fg="#f0ebf5",
                                     command=download_for_youtube)
    youtube_download_button.grid(row=2, column=1, padx=30, pady=30)
    #youtube_download_back_button = Button(youtube,text="Back",bg="#7e8987" , font= "Georgia 45 italic bold" , fg= "#f0ebf5" , command= menu)
    #youtube_download_back_button.grid(row=2 ,column=2 ,padx=30 , pady=30 )


def download_for_youtube():
    url = youtube_url_textbox1.get()
    qualityofvideo = youtube_url_textbox2.get()
    download_video(url, qualityofvideo)
    #do your bullshit here


def soundcloud_download():
    soundcloud_frame = Tk()
    soundcloud_frame.title("universal downloader")
    soundcloud_frame.config(bg="#2e3440")
    soundcloud_frame.geometry("1800x700")
    soundcloud_label1 = Label(soundcloud_frame,
                              text="enter the url of the song",
                              font="Georgia 25 italic bold",
                              fg="#7e8987",
                              bg="#2e3440")
    soundcloud_label1.grid(row=0, column=0, padx=30, pady=30)
    global soundcloud_textbox1
    soundcloud_textbox1 = Entry(soundcloud_frame, width=70)
    soundcloud_textbox1.grid(row=0, column=1, padx=30, pady=30)
    soundcloud_download_button = Button(soundcloud_frame,
                                        text="Download",
                                        bg="#7e8987",
                                        font="Georgia 45 italic bold",
                                        fg="#f0ebf5",
                                        command=download_for_soundcloud)
    soundcloud_download_button.grid(row=2, column=1, padx=30, pady=30)


def download_for_soundcloud():
    url = soundcloud_textbox1.get()
    soundcloud(url)


def soptify_download():
    soptify_frame = Tk()
    soptify_frame.title("universal downloader")
    soptify_frame.config(bg="#2e3440")
    soptify_frame.geometry("1800x700")
    soptify_label1 = Label(soptify_frame,
                           text="enter the url of the song",
                           font="Georgia 25 italic bold",
                           fg="#7e8987",
                           bg="#2e3440")
    soptify_label1.grid(row=0, column=0, padx=30, pady=30)
    global soptify_textbox1
    soptify_textbox1 = Entry(soptify_frame, width=70)
    soptify_textbox1.grid(row=0, column=1, padx=30, pady=30)
    soptify_download_button = Button(soptify_frame,
                                     text="Download",
                                     bg="#7e8987",
                                     font="Georgia 45 italic bold",
                                     fg="#f0ebf5",
                                     command=download_for_soptify)
    soptify_download_button.grid(row=2, column=1, padx=30, pady=30)


def download_for_soptify():
    url = soptify_textbox1.get()
    spotify(url)


def download_for_wallpaper():
    wallpaper_frame = Tk()
    wallpaper_frame.title("universal downloader")
    wallpaper_frame.config(bg="#2e3440")
    wallpaper_frame.geometry("1800x700")
    wallpaper_label1 = Label(wallpaper_frame,
                             text="enter the url ",
                             font="Georgia 25 italic bold",
                             fg="#7e8987",
                             bg="#2e3440")
    wallpaper_label1.grid(row=0, column=0, padx=30, pady=30)
    global wallpaper_url_textbox1
    global wallpaper_url_textbox2
    wallpaper_url_textbox1 = Entry(wallpaper_frame, width=70)
    wallpaper_url_textbox1.grid(row=0, column=1, padx=30, pady=30)
    wallpaper_label2 = Label(
        wallpaper_frame,
        text="Enter the number of images or enter 0 to cancel:",
        font="Georgia 25 italic bold",
        fg="#7e8987",
        bg="#2e3440")
    wallpaper_label2.grid(row=1, column=0, padx=30, pady=30)
    wallpaper_url_textbox2 = Entry(wallpaper_frame, width=70)
    wallpaper_url_textbox2.grid(row=1, column=1, padx=30, pady=30)
    wallpaper_download_button = Button(
        wallpaper_frame,
        text="Download",
        bg="#7e8987",
        font="Georgia 45 italic bold",
        fg="#f0ebf5",
        command=download_for_wallpaper_execution)
    wallpaper_download_button.grid(row=2, column=1, padx=30, pady=30)


def download_for_wallpaper_execution():
    url = wallpaper_url_textbox1.get()
    num = wallpaper_url_textbox2.get()

    download_wallpapers(url, num)


unvirsal_downloader = Tk()
unvirsal_downloader.title("universal downloader")
unvirsal_downloader.config(bg="#2e3440")
unvirsal_downloader.geometry("800x600")
wlecome_label = Label(unvirsal_downloader,
                      text="Welcome",
                      font="Georgia 45 italic bold",
                      fg="#7e8987",
                      bg="#2e3440")
wlecome_label.pack(pady=40, fill=Y, expand=True)
start_button = Button(unvirsal_downloader,
                      text="Start",
                      bg="#7e8987",
                      font="Georgia 45 italic bold",
                      fg="#f0ebf5",
                      command=menu)
start_button.pack(fill=Y, expand=True)
exit_button = Button(unvirsal_downloader,
                     text="Exit",
                     bg="#7e8987",
                     font="Georgia 45 italic bold",
                     fg="#f0ebf5",
                     command=exit)
exit_button.pack(pady=40, fill=Y, expand=True)

unvirsal_downloader.mainloop()
