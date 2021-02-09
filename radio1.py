from tkinter import *
from tkinter import messagebox as tmsg
root = Tk()
root.geometry("275x375")
root.title("Radio Model")
def getorder():
    print(f"your oreder for {m.get} is taken /n thanks for ordering")
    tmsg.showinfo("submited oreer", f"your oreder for {m.get} is taken /n thanks for ordering")
Label(root, text = "what you want sir", padx=19, font="lucida 19 bold").pack()
item=["pratha","dosa","full paneer thali", "sadi thali", "samosa"]
var = StringVar()
var.set(item[0])

for i in range(len(item)):
    radio = Radiobutton(root, text=i, variable=var, value=i,padx=19).pack(anchor="w")
m =radio.value
Button(root, text="order now", padx=19, command =getorder()).pack()
root.mainloop()
