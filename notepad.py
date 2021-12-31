from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import os   
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *



root = Tk()
root.geometry('1280x720')

file = None

def open_text():
    global text_file
    text_file = filedialog.askopenfilename(title="Open text File", filetypes=(("Text Files", "*.txt"), ))
     
    text_file = open(text_file,  'r')
    stuff = text_file.read()

    entry.insert(END, stuff)
    text_file.close()


def saveas():
    text_file = asksaveasfilename(initialfile='Untitled.txt',
											defaultextension=".txt",
											filetypes=[("All Files","*.*"),
												("Text Documents","*.txt")])
    text_file = open(text_file, 'w')
    text_file.write(entry.get(1.0, END))

def save():
    text_file = asksaveasfilename(initialfile='Untitled.txt',
											defaultextension=".txt",
											filetypes=[("All Files","*.*"),
												("Text Documents","*.txt")])
    text_file = open(text_file,"w")
    text_file.write(entry.get(1.0,END))
    text_file.close()


    
def newFile():
    root.title("Untitled - Notepad")
    file = None
    entry.delete(1.0,END)



menubar = Menu(root)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Settings', menu = filemenu)
filemenu.add_command(label = "Copy to clipboard")
filemenu.add_command(label = "Open", command=open_text)
filemenu.add_command(label = "Save", command=save)
filemenu.add_command(label = "New", command=newFile)

root.config(menu=menubar)

frame = Frame(root).place(x=0, y=0)

entry = Text(frame, height = 30, width = 125)
entry.place(x=125, y=90)







root.mainloop()