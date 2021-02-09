from tkinter import *
root =Tk()
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os  
root.title("notepad")
root.geometry("644x686")
def newFile():
    global file
    root.title("Untiled - Notepad")
    file = NONE
    TextArea.delete(1.0, END) 

def openFile():
    global file

def saveFile():
    pass
def SaveAs():
    pass
def quitapp():
    pass
def CutFile():
    pass
def pasteFile():
    pass
def CopyFile():
    pass
def Undodata():
    pass
def redodata():
    pass
#text area
TextArea= Text(root, font="Lucida 13")
file =None
#creating a menu bar
menuBar= Menu(root)
############ File menu start
FileMenu= Menu(menuBar, tearoff=0)
#to open new file 
FileMenu.add_command(label="New",command = newFile)
#to open alredy exicting file 
FileMenu.add_command(label = "Open", command= openFile)
#to save File 
FileMenu.add_command(label ="save", command=saveFile)
# For using save as file 
FileMenu.add_command(label="Save as", command = SaveAs)
#adding seprater 
FileMenu.add_separator()
FileMenu.add_command(label="exit", command=quitapp)

menuBar.add_cascade(label="File", menu = FileMenu)

################### file menu end
##### edit menu start
EditMenu=Menu(menuBar, tearoff=0)
EditMenu.add_command(label="cut", command= CutFile )
EditMenu.add_command(label="Copy", command=CopyFile)
EditMenu.add_command(label="Paste", command= pasteFile )
EditMenu.add_separator()

EditMenu.add_command(label="undo", command=Undodata)
EditMenu.add_command(label="Redo", command=redodata)

root.config(menu=menuBar)
root.config(=EditMenu)

root.mainloop()