from tkinter import *
root=Tk()
def upload():
    statusvar.set("busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")

root.geometry("455x455")
root.title("status bar")

statusvar =StringVar()
statusvar.set("Reday now")
sbar = Label(root, textvariable= statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="uplod", command=upload).pack()
root.mainloop()