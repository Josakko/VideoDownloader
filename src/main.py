from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


def select_path():
    
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file(): 
    
    get_link = link_field.get()
    
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    screen.iconbitmap("JK.ico")
    screen.resizable(False, False)
    screen.config(bg="#dbdbdb")
    
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another Video...')

screen = Tk()
title = screen.title('Youtube Downloader')
screen.config(bg="#dbdbdb")
screen.iconbitmap("JK.ico")
screen.resizable(False, False)
canvas = Canvas(screen, width=500, height=500)
canvas.config(bg="#dbdbdb")
canvas.pack()


img = PhotoImage(file='yt.png')

img = img.subsample(2, 2)
canvas.create_image(250, 80, image=img)


link_field = Entry(screen, width=40,bg="#babbbc", font=('Arial', 15) )
link_label = Label(screen, text="Enter Download Link: ",bg="#dbdbdb",fg="black", font=('Arial', 15))


path_label = Label(screen, text="Select Path For Download",bg="#dbdbdb", font=('Arial', 15), fg="black")
select_btn =  Button(screen, text="Select Download Directory", bg="#dbdbdb", padx="22", pady="5",font=("Arial", 15), fg="black", command=select_path, width=20)

canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

download_btn = Button(screen, text="Download Video", bg="#dbdbdb", padx='22', pady='5',font=('Arial', 15), fg='black', command=download_file, width=20)

canvas.create_window(250, 390, window=download_btn)

screen.mainloop()