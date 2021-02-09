from tkinter import *
root = Tk()
l= 200
m= 300
root.geometry(f"{l}x{m}")
def anand():
    l = lavalue.get()
    m = mvalue.get()

l.grid(padx=23,pady=13)
m.grid(padx=24,pady=13)

lavalue = IntVar()
mvalue =IntVar() 

lentry = Entry(root, textvariable = lvalue) 
mentry =Entry(root, textvariable= mvalue)  

lentry.grid(row= 0, column= 1)
mentry.grid(row=1, column=1)
Button(text="submit", COMMAND= anand).grid()
root.mainloop()

