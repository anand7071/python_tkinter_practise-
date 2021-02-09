from tkinter import *
from tkinter import messagebox as tmsg
root = Tk()
def getdoller():
    print(f"your {myslider.get()} balance is credited in account")
    tmsg.showinfo("amount credited", f"your {myslider.get()} balance is credited in account")
root.geometry("273x273")
root.title("Slider")

Label(root, text="how many doller you want?").pack()
myslider = Scale(root, from_=10, to=100, orient= HORIZONTAL, tickinterval=10)
myslider.set("50")
myslider.pack()
Button(root, text= "getdoller", pady=10, command=getdoller).pack()

root.mainloop()

