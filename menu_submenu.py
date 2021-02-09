from tkinter import *
root =Tk()
root.geometry("253x263")
root.title("my GUI")
def func12():
    print("akash bhoshdi ka gaad dega yaha dabane pe")

mainmenu = Menu(root)
mainmenu.add_command(label="File", command= func12)
mainmenu.add_command(label= "quit", command= quit)
root.config(menu=mainmenu)


m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="new project", command=func12)
m1.add_command(label="save", command=func12)
m1.add_command(label ="saveas", command=func12)
m1.add_command(label="print", command=func12)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="file", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="cut", command=func12)
m2.add_command(label="copy", command=func12)
m2.add_command(label ="edit", command=func12)
m2.add_command(label="undo", command=func12)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="mmm", menu=m2)


root.mainloop()
