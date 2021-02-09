
from tkinter import *
root = Tk()
root.geometry("700x711")

def getvals():
    print(f"the username is {uservalue.get()}")
    print(f"the passward is {passvalue.get()}")

user = Label(root, text="username") 
passward= Label(root, text="Passwerd")
user.grid()
passward.grid()

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
Button(text="submit", command=getvals()).grid()

root.mainloop()