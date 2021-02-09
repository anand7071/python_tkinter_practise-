from tkinter import *
root =Tk()
#============================

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scvalue.get()) 
        scvalue.set(value)
        screen.update       
    if text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    if text == "x":
        scvalue.set("")
        screen.update()
        
root.geometry("644x900")

#========================
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx= 10, padx=10)
#========================

f = Frame(root, bg="grey")
b = Button(f, text="c", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side= LEFT,padx=13,pady=9)
b.bind("<Button-1>", click)
f.pack()

b = Button(f, text="/", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side=LEFT,padx=13,pady=9)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side = LEFT,padx=12,pady=9)
b.bind("<Button-1>", click)

b = Button(f, text="x", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side = LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)

f.pack()

#==================================

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=12, pady=8 ,font ="lucida 35 bold")
b.pack(side= LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)
f.pack()

b = Button(f, text="8", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side = LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side = LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)

f.pack()
#=========================
f = Frame(root, bg="grey")
b = Button(f, text="6", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side= LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)
f.pack()

b = Button(f, text="5", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side = LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side = LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)

f.pack()
#===============================
f = Frame(root, bg="grey")
b = Button(f, text="3", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side= LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)
f.pack()

b = Button(f, text="2", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side = LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side = LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)

f.pack()
#================================

f = Frame(root, bg="grey")
b = Button(f, text="%", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side= LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)
f.pack()

b = Button(f, text="0", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side=LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=12, pady=8, font ="lucida 35 bold")
b.pack(side = LEFT,padx=12,pady=8)
b.bind("<Button-1>", click)

b = Button(f, text="mc", padx=10, pady=8, font ="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=8)
b.bind("<Button-1>", click)

f.pack()
root.mainloop()
