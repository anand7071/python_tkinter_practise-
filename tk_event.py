from tkinter import *
root= Tk()
def anand(event):
    print(f"you clicked on the button at {event.x},{event.y} ")
m=200
t=300
root.geometry(f"{m}x{t}")
root.title("my event")
Widget = Button(root, text= "clck now")
Widget.pack()
Widget.bind('<Button-1>',anand)
Widget.bind('<Double-1>',quit)
root.mainloop()