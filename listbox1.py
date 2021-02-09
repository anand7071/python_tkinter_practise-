from tkinter import *
root =Tk()

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1
root.geometry("271x500")
root.title("ListBox")
i=0    
lbx= Listbox(root)
lbx.pack()
lbx.insert(END , "first item of list box ")
Button(root, text="add", command=add).pack()
root.mainloop()