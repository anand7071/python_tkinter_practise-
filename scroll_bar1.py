from tkinter import *
root =Tk()
root.geometry("235x2377")
root.title("scrol bar")

def add():
    global i 
    lst.insert(ACTIVE, f"{i}")
    i+=1
i=0
lst=Listbox(root)
lst.pack()
lst.insert(END, "first item of list box")
Button(root, text="add", command=add).pack()

Scrollbar=Scrollbar(root)
Scrollbar.pack(side=RIGHT, fill=Y)
lst =Listbox(root, yscrollcommand=Scrollbar.set)
for i in range(344):
    lst.insert(END, f"{i}")
lst.pack(fill="both")  
root.mainloop()