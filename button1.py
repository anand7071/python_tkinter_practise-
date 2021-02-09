from tkinter import *

root = Tk()
root.geometry("458x452")

def hello():
    print("HEllo tkinter Button")

def name():
    print("name is ghnashyam")

frame = Frame(root, borderwidth=7, bg='grey', relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")
b1= Button(frame,fg="red", text="print now", command=hello)
b1.pack(side=LEFT, padx=34)
b2= Button(frame,fg="red", text="name", command=name)
b2.pack(side=RIGHT, padx=34)

root.mainloop()