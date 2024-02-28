from tkinter import *
import ttkbootstrap as tb

def click(event):
    sc.config(state=NORMAL)
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(sc.get())
        scvalue.set(value)
        sc.update()        
        
    elif text == "C":
        scvalue.set("")
        sc.update()
    else:
        scvalue.set(scvalue.get() + text)
        sc.update()
    sc.config(state=DISABLED)
        
root = tb.Window(themename="darkly")
root.geometry("450x550")
root.title("Calculator")
root.minsize(450, 600)
root.maxsize(450, 600)
root.configure(padx=17, pady=22)

f = tb.Frame(root)
# Text label and Output Entry
scvalue = StringVar(value="")
tb.Label(f, 
        text="Result :", 
        font="classic 20 bold", 
        bootstyle="info").pack(padx=15, pady=12)
sc = tb.Entry(f, 
        textvariable=scvalue, 
        font="classic 25 bold", 
        foreground="white",
        width=25)
sc.pack(padx=18, ipadx=15, ipady=8)
sc.config(state=DISABLED, width="18")
f.pack()

# Buttons Style
tb.Style().configure("TButton", font="classic 28 bold", width=3)
iypading = 7
xpading = 2
ypading = 2

# Buttons Frame
mainf = tb.Frame(root)
for i in range(5):
    f = tb.Frame(root)
    match(i):
        case 0:
            b = tb.Button(f, text=".", style="TButton")
            b.pack(padx=xpading, pady=ypading, side=LEFT, ipady=iypading)
            b.bind("<Button-1>", click)
            
            b = tb.Button(f, text="0", style="TButton")
            b.pack(padx=xpading, pady=ypading, side=LEFT, ipady=iypading)
            b.bind("<Button-1>", click)
            
            b = tb.Button(f, text="00", style="TButton")
            b.pack(padx=xpading, pady=ypading, side=LEFT, ipady=iypading)
            b.bind("<Button-1>", click)
            
            b = tb.Button(f, text="=", style="TButton")
            b.pack(padx=xpading, pady=ypading, side=LEFT, ipady=iypading)
            b.bind("<Button-1>", click)
            
        case 1:
            for j in range(3):
                b = tb.Button(f, text=f"{j+1}", style="TButton")
                b.pack(side=LEFT, padx=xpading, pady=ypading, ipady=iypading)
                b.bind("<Button-1>", click)
                
            b = tb.Button(f, text="+", style="TButton")
            b.pack(padx=xpading, pady=ypading, side=LEFT, ipady=iypading)
            b.bind("<Button-1>", click)
                
        case 2:
            for j in range(4, 7):
                b = tb.Button(f, text=f"{j}", style="TButton")
                b.pack(side=LEFT, padx=xpading, pady=ypading, ipady=iypading)
                b.bind("<Button-1>", click)
                
            b = tb.Button(f, text="-", style="TButton")
            b.pack(padx=xpading, pady=ypading, side=LEFT, ipady=iypading)
            b.bind("<Button-1>", click)
                
        case 3:
            for j in range(7, 10):
                b = tb.Button(f, text=f"{j}", style="TButton")
                b.pack(side=LEFT, padx=xpading, pady=ypading, ipady=iypading)
                b.bind("<Button-1>", click)
                
            b = tb.Button(f, text="*", style="TButton")
            b.pack(padx=xpading, pady=ypading, side=LEFT, ipady=iypading)
            b.bind("<Button-1>", click)
                
        case 4:
            b = tb.Button(f, text="%", style="TButton")
            b.pack(padx=xpading, pady=ypading, side=LEFT, ipady=iypading)
            b.bind("<Button-1>", click)
            
            b = tb.Button(f, text="C", style="TButton")
            b.pack(padx=xpading, pady=ypading, side=LEFT, ipady=iypading)
            b.bind("<Button-1>", click)
            
            b = tb.Button(f, text="<=", style="TButton")
            b.pack(padx=xpading, pady=ypading, side=LEFT, ipady=iypading)
            b.bind("<Button-1>", click)
            
            b = tb.Button(f, text="/", style="TButton")
            b.pack(padx=xpading, pady=ypading, side=LEFT, ipady=iypading)
            b.bind("<Button-1>", click)
            
    f.pack(side=BOTTOM)
mainf.pack()
# Buttons Frame

root.mainloop()