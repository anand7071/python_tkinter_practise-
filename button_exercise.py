from tkinter import *
root = Tk()
root.geometry("325x254")
root.title("gym application form")
 
def getvals():
    print(f"the user name is {namevalue.get()}")
    print(f"the user father name is {father_namevalue.get()}")
    print(f"the user age is{agevalue.get()}")
    print(f"the user date of joining \t{date_OF_joiningvalue.get()}")

    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), father_namevalue.get(), agevalue.get(), date_OF_joiningvalue.get()}\n")
name = Label(root, text="user name")
father_name =Label(root, text="father name")
age = Label(root, text="age")
date_OF_joining = Label(root, text="date of joining")
name.grid(padx=23,pady=13)
father_name.grid(padx=23,pady=13)
age.grid(padx=23,pady=13)
date_OF_joining.grid(padx=23,pady=13)

namevalue = StringVar()
father_namevalue = StringVar()
agevalue = StringVar()
date_OF_joiningvalue = StringVar()

nameentry = Entry(root, textvariable=namevalue)
father_nameentry = Entry(root, textvariable=father_namevalue)
agevalueentry = Entry(root, textvariable=agevalue)
date_OF_joiningentry = Entry(root, textvariable=date_OF_joiningvalue)

nameentry.grid(row=0, column=1)
father_nameentry.grid(row=1, column=1)
agevalueentry.grid(row=2, column=1)
date_OF_joiningentry.grid(row=3, column=1)
Button(text="submit", command=getvals).grid()

root.mainloop()