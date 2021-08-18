from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("700x500")
load = Image.open("C:\\Users\\Manav\\Downloads\\MP\\MP-1\\web1.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img.place(x=0 , y=0)
root.mainloop()