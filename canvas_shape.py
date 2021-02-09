from tkinter import *
import os 

root = Tk()
t= 800
m= 700
root.title("canvas_heare")
root.geometry(f"{t}x{m}")

can_widget= Canvas(root, width=t, height=m)
can_widget.pack()
can_widget.create_line(5,6,600,460)
can_widget.create_line(6,600,450,5)

can_widget.create_oval(101,200,500,600)
can_widget.create_rectangle(101,200,500,600)
can_widget.create_bitmap(200,600)
can_widget.create_arc(200,200,400,400)
can_widget.create_window(100,200,200,200)   

root.mainloop()
