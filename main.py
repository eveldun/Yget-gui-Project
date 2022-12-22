import tkinter
from tkinter import *
from PIL import ImageTk
from PIL import Image as Image

Dark50 = "#FAFAFA"
Dark100 = "#F5F5F5"
Dark200 = "#EEEEEE"
Dark300 = "#E0E0E0"
Dark400 = "#BDBDBD"
Dark500 = "#9E9E9E"
Dark600 = "#757575"
Dark700 = "#616161"
Dark800 = "#424242"
Dark900 = "#212121"
Purp = "#963297"
# I know this is inefficient but if i lay it out like this i can get a better concept of a good color pallete
#Window Settings
Win = tkinter.Tk()
Win.configure(bg=Dark800)  # Backround
Win.title("Yget - Open Source Youtube Downloader")
Win.geometry("800x400")
def OnLeave(event):
    SettingsButton.config(text="Settings", bg=Dark800, fg=Dark300, highlightcolor=Dark900, highlightbackground = Dark900)
def OnEnter(event):
    SettingsButton.config(Win, text="Settings", bg=Dark700, fg=Dark300, highlightcolor=Dark900, highlightbackground = Dark900)

SettingsButton = tkinter.Button(Win, text="Settings", bg=Dark800, fg=Dark300, highlightcolor=Dark900, highlightbackground = Dark900)
SettingsButton.place(x=0, y=0)
SettingsButton.bind("<Enter>",OnEnter())
SettingsButton.bind("<Leave>",OnLeave)


IntroText = tkinter.Label(Win, text="Yget - Youtube Video Downloader", font="System", fg=Dark300, bg=Dark800)
IntroText.place(y=5, x=85)


YoutubeURL = tkinter.Entry(Win, textvariable="yurl", bg=Dark800, fg=Dark300, bd=0, highlightcolor=Purp,highlightbackground = Purp,width=50,selectbackground=Dark800,)
YoutubeURL.insert(0,"Type in a youtube link or playlist")
YoutubeURL.tkraise()
YoutubeURL.place(y=190, x=140,width=450)

Stuff = Frame(Win)
Stuff.pack()
photoimage = ImageTk.PhotoImage(Image.open("LogoForGit.png"))
width, height = photoimage.width(), photoimage.height()
canvas = Canvas(Win, bg=Dark800, width=width, height=height,highlightthickness=0)
canvas.pack()
canvas.place(y=35,x=150)
canvas.create_image(0, 0, image=photoimage, anchor=NW)

Win.resizable(width=False, height=False)
Win.mainloop()
