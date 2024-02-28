from tkinter import *
import ttkbootstrap as tb
import requests

def download():
    status.configure(text=f"File Downloading...")
    status.update()
    
    url = fileurl.get()
    
    r = requests.get(url)
    
    if saveas.get() == "":
        savename = "new"+extension.get()
    else:
        savename = saveas.get()+extension.get()
    
    with open(savename, "wb") as f:
        f.write(r.content)
    
    status.configure(text=f"Downloaded file as {savename}")

root = tb.Window(themename="superhero")
root.geometry("500x400")
root.title("Download File")

tb.Label(root, text="Downlaod File", font="classic 16 bold underline").pack(pady=10)

# f1 start
f1 = tb.Frame(root)

# file url
tb.Label(f1, text="File Url:", font="classic 14 bold").grid(row=1, column=1, padx=10, pady=15)

fileurl = tb.Entry(f1, font="classic 10")
fileurl.grid(row=1, column=2, padx=10, pady=15)

# save as
tb.Label(f1, text="Save as:", font="classic 14 bold").grid(row=2, column=1, padx=10, pady=15)

saveas = tb.Entry(f1, font="classic 10")
saveas.grid(row=2, column=2, padx=10, pady=15)

# combobox
l = [".jpg", ".jpeg", ".png"]
extension = tb.Combobox(f1, values=l, width=5, font="clasic 10 bold")
extension.set(l[0])
extension.grid(row=2, column=3)

f1.pack(pady=10)
# f1 end

# button & button style
tb.Style().configure("success.Outline.TButton", font="classic 12 bold")

tb.Button(root,text="Download", style="success.Outline.TButton", command=download).pack(pady=20)

# status
status = tb.Label(root, text="Status:", font="classic 14 bold")
status.pack(pady=20)

root.mainloop()