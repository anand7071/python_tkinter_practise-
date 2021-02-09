# from PIL import Image, ImageTk 
from tkinter import *
m_root = Tk()
m_root.geometry('644x344')
m_root.title("my computr")
title_label = Label(text = "MY computer is a folder \n that contains the file and folder and its have all contain \n which are stored in the driver",bg = "black", fg='green', padx=560, pady=560, font="comicsansms 9 bold", borderwidth= 3, relief=GROOVE )
title_label.pack(side=RIGHT, fill=X, padx=10, pady=10)
m_root.maxsize(999, 988)
m_root.minsize(345, 200)

m_root.mainloop()


