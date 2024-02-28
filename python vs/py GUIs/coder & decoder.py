from tkinter import *
import random as r
import os
    
def coding():
    code = text_value.get()
    words = code.split(" ")
    l = "abcdefghijklmnopqrstuvwxyz"
    nwords = []
    for word in words:
        if (len(word) >= 3):
            newcode = r.choice(l)+r.choice(l)+r.choice(l)+word[1:]+word[0]+r.choice(l)+r.choice(l)+r.choice(l)
            nwords.append(newcode)
        else:
            nwords.append(word[::-1])
    str = " ".join(nwords)
    print(str)
    Label(root, text=str, font="classic 14", bg="light gray").pack(pady=10)
    
def decoding():
    code = text_value.get()
    words = code.split(" ")
    nwords = []
    for word in words:
        if (len(word) >= 3):
            newcode = word[3:-3]
            newcode = newcode[-1] + newcode[:-1]
            nwords.append(newcode)
        else:
            nwords.append(word[::-1])
    str = " ".join(nwords)
    print(str)
    Label(root, text=str, font="classic 14", bg="light gray").pack(pady=10)

root = Tk()
root.title(os.getcwd())
root.geometry("700x500")
root.configure(bg="light gray")

Label(text="Coder and Decoder by Rajat Bhai", font="classic 20 bold underline", fg="dark blue", bg="light gray").pack(pady=15)

text_value = StringVar()
text_entry = Entry(root, textvariable=text_value, width=80)
text_entry.pack(pady=18)

f1 = Frame(root, width=550, height=50, bg="light gray")
Button(f1, text="Code", font="classic 10 bold", bg="light gray", height=2, width=13, command=coding).grid(row=1, column=1, padx=40, pady=18)
Button(f1, text="Decode", font="classic 10 bold", bg="light gray", height=2, width=13, command=decoding).grid(row=1, column=2, padx=40, pady=18)
f1.pack()

Label(root, text="Output:-", font="classic 16 bold underline", fg="blue", bg="light gray").pack()

root.mainloop()
