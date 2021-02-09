from tkinter import *
m_root = Tk()
m_root.geometry('644x344')
m_root.title("my computr")
def hello():
    pass
b1= Button(fg="red", text="printnow", command=hello )
b1.pack(side=LEFT, padx=23)
m_root.maxsize(999, 988)
m_root.minsize(345, 200)
m_root.mainloop()