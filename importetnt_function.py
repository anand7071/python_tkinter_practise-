from tkinter import *
root = Tk()
root.geometry("155x256")
root.title("my Gui")
# root.wm_iconbitmap("i.ico")#icon downlod from internet
root.configure(background = "grey")

width =root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="close", command =root.destroy).pack()


root.mainloop()


