from tkinter import *
import random
import urllib.request

def web_image(url):
    name = random.randrange(1,1000)
    fullName = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullName)

def download():
    web_image(downloadEntry.get())

root = Tk()

frame = Frame(root, width=500, height=500)
frame.pack()

url = Label(frame, text="Image Url")
url.grid(row=0, column=0)

downloadEntry = Entry(frame)
downloadEntry.grid(row=0,column=1)
downloadButton = Button(frame, text="Download Now", command=download)
downloadButton.grid(row=1,columnspan=2)

root.mainloop()