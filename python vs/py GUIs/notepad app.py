from tkinter import *
from tkinter.messagebox import showinfo
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename

def Newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)

def Openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")])
    
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        textarea.delete(1.0, END)
        with open(file, "r") as f:
            textarea.insert(1.0, f.read())
            
def Savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")])
        if file == "":
            file = None
        else:
            # Save as a new file
            with open(file, "w") as f:
                f.write(textarea.get(1.0, END))
                
            root.title(os.path.basename(file)+" - Notepad")
    else:
        # Save the file
        with open(file, "w") as f:
            f.write(textarea.get(1.0, END))
def Closefile():
    root.destroy()

def Cut():
    textarea.event_generate(("<<Cut>>"))

def Copy():
    textarea.event_generate(("<<Copy>>"))

def Paste():
    textarea.event_generate(("<<Paste>>"))

def About():
    showinfo("About", "Notepad Made By Rajat")

root = Tk()
root.title("Untitled - Notepad")
root.geometry("650x700")

mainmenu = Menu(root)

# File Menu Start
Filemenu = Menu(tearoff=0)
Filemenu.add_command(label="New", command=Newfile)
Filemenu.add_command(label="Open", command=Openfile)
Filemenu.add_command(label="Save", command=Savefile)
Filemenu.add_command(label="Close", command=Closefile)
mainmenu.add_cascade(label="File", menu=Filemenu)
# File Menu End

# Edit Menu Start
Editmenu = Menu(tearoff=0)
Editmenu.add_command(label="Cut", command=Cut)
Editmenu.add_command(label="Copy", command=Copy)
Editmenu.add_command(label="Paste", command=Paste)
mainmenu.add_cascade(label="Edit", menu=Editmenu)
# Edit Menu End

# Help Menu Start
Helpmenu = Menu(tearoff=0)
Helpmenu.add_command(label="About", command=About)
mainmenu.add_cascade(label="Help", menu=Helpmenu)
# Help Menu End

# configuring mainmenu
root.config(menu=mainmenu)

# Scrollbar
sbar = Scrollbar()
sbar.pack(side=RIGHT, fill=Y)

# Text Area
textarea = Text(root, font="classic 14")
textarea.pack(fill=BOTH, expand=TRUE)
file = None

# Binding Scrollbar
sbar.config(command=textarea.yview)
textarea.config(yscrollcommand=sbar.set)

root.mainloop()