import tkinter
from tkinter import *
from PIL import Image, ImageTk

import tkinter.messagebox
root = tkinter.Tk()
root.title("Mystery Of Edencrest Manor")
root.geometry("500x750")
Width, Height = 500, 750


canvas = tkinter.Canvas(root, width=Width, highlightthickness=0)
canvas.pack(side = "bottom", fill="both", expand="yes")

path_of_image = 'coverart.jpg'
image1 = ImageTk.PhotoImage(Image.open(path_of_image))
canvas.create_image(250, 400, image=image1)

title = "Mystery of Edencrest Manor"
canvas.create_text(250, 200, text="Mystery Of Edencrest Manor", font="Terminal 20", fill='white')


def start():
    root.destroy()
    import App


startButton = Button(root, text="Start", font=("Terminal",10), command=start, height=2, width=10)
startButton.place(x = 205, y = 600)


root.mainloop()