'''Author: Sams KHan
Class: User Interface Engineering
References: https://www.youtube.com/watch?v=xqDonHEYPgA
            https://www.instructables.com/id/Create-a-Simple-Python-Text-Editor/
'''




import sys
from tkinter import *
import tkinter.filedialog as fd
root = Tk()

#Adding text widget
text = Text(root)
text.grid()

'''#Adding ability to save file
def save():
    global text
    t=text.get(0.0,END)
    f=open(text,'w')
    f.write(t)
    f.close()'''
#New file
def new():
    global filename
    filename = "Untitled"
    text.delete(0.0,END)

def openFile():
    f=fd.askopenfile(mode='r')
    t=f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)

#Adding the ability to save as
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = fd.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

root.title("Word Processor")

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save as", command=saveas)
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)
root.config(menu=menubar)
root.mainloop()