import tkinter
from tkinter import *
from PIL import ImageTk
from PIL import Image as Image
from tkinter import ttk
import os
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

def DonateClicked():
    os.system("xdg-open https://github.com/eveldun/Yget/blob/master/Misc/donate.md")
def SourceClicked():
    os.system("xdg-open https://github.com/eveldun/Yget/")
def CreditsClicked():
    os.system("xdg-open https://github.com/eveldun/Yget/blob/master/Credits")

IntroText = tkinter.Label(Win, text="Yget - Youtube Video Downloader", font="System", fg=Dark300, bg=Dark800)
IntroText.place(y=5, x=0)

CopyRight = tkinter.Label(Win, text="Copyright (c) 2022 Eveldun. Some rights reserved.", font="System", fg=Dark300, bg=Dark800)
CopyRight.place(y=385, x=151)
CopyRight.config(font=("Arial",8))

DownloadButton = Button(Win, text="Download",bg=Dark800, fg=Dark300, highlightcolor=Dark900, highlightbackground = Dark900,padx=1,pady=1)
DownloadButton.place(y=188,x=655)

DonateButton = Button(Win, text="Donate",bg=Dark800, fg=Dark300, highlightcolor=Dark900, highlightbackground = Dark900,padx=1,pady=1,borderwidth=0,command=DonateClicked)
DonateButton.place(y=380,x=0)

CreditsButton = Button(Win, text="Credits",bg=Dark800, fg=Dark300, highlightcolor=Dark900, highlightbackground = Dark900,padx=1,pady=1,borderwidth=0,command=CreditsClicked)
CreditsButton.place(y=380,x=100)

ProjectPage = Button(Win, text="Source",bg=Dark800, fg=Dark300, highlightcolor=Dark900, highlightbackground = Dark900,padx=1,pady=1,borderwidth=0,command=SourceClicked)
ProjectPage.place(y=380,x=51)
x= tkinter.StringVar()
FileFormat = ttk.Combobox(Win,width=5,textvariable=x)
FileFormat['values']=('Mp4' , 'Mp3' , 'Ogg')
FileFormat.place(x=595,y=189)

combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {
                                       'selectbackground': Dark800,
                                       'inactiveselectbackground': Dark800,
                                       'fieldbackground': Dark800,
                                       'background': Dark700
                                       }}}
                         )
# ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
combostyle.theme_use('combostyle')

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
