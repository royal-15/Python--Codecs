from tkinter import *
import os
import requests
import ttkbootstrap as tb

def search():
    statusvar.set("Searching...")
    result_label.update()
    query = news_value.get()
    description = description_value.get()
    content = content_value.get()
        
    url = f"https://newsapi.org/v2/everything?q={query}&popularity&apiKey=d1f69ee125ac4256bf0c651883d3dafa"
    news = requests.get(url).json()
    
    text.config(state=NORMAL)
    text.delete(1.0, END)
    i = 0
    statusvar.set("Results")
    for article in news["articles"]:
        # print(f"\n {i+1}. {article["title"]} :\n")
        text.insert(END, f"\n {i+1}. {article["title"]} :\n")
        # print(f"{article["description"]}\n") if description == 1 else ""
        text.insert(END, f"{article["description"]}\n") if description == 1 else ""
        # print(article["content"]) if content == 1 else ""
        text.insert(END, article["content"]) if content == 1 else ""
        text.insert(END, "\n")
        i = i + 1
    text.config(state=DISABLED)
    news_value.set("")

root = tb.Window(themename="superhero")
root.title(os.getcwd())
root.geometry("820x600")

# Heading Label
tb.Label(root, text="News App By Rajat", font="classic 20 bold").pack(pady=10)

# Frame 1
f1 = Frame(root, width=400, height=25, bg="light gray")

tb.Label(f1, text="News:", font="classic 14 bold").grid(row=1, column=1, padx=3)

news_value = StringVar()
news_entry = tb.Entry(f1, textvariable=news_value, width=18, font="classic 12 bold")
news_entry.grid(row=1, column=2, padx=10)

description_value = IntVar()
content_value = IntVar()

# Style
tb.Style().configure("success.TCheckbutton", font="classic 12 bold")
tb.Style().configure("success.Outline.TButton", font="classic 10 bold")

# Description
description_box = tb.Checkbutton(f1, text="Description", bootstyle="info", variable=description_value, onvalue=1, offvalue=0, style="success.TCheckbutton")
description_box.grid(row=1, column=3, padx=10)

# Content
Content_box = tb.Checkbutton(f1, text="Content", bootstyle="info", variable=content_value, onvalue=1, offvalue=0, style="success.TCheckbutton")
Content_box.grid(row=1, column=4, padx=10)

# search button
search_button = tb.Button(f1, text="Search", style="success.Outline.TButton", command=search)
search_button.grid(row=1, column=11, padx=3)

f1.pack(pady=8, padx=15)
# Frame 1

# Result Label & Varialble
statusvar = StringVar()
result_label = tb.Label(root, textvariable=statusvar,  font="classic 14 bold")
result_label.pack(pady=2)

# Scrollbar & Text Area
scrollbar = tb.Scrollbar(root)
scrollbar.pack(side=RIGHT, fill="both", pady=12)

text = Text(root, width=100, height=50, yscrollcommand=scrollbar.set, wrap="word")
text.configure(font="classic 14 bold")
text.pack(fill="both", padx=25, pady=12)
text.config(state=DISABLED)

scrollbar.config(command=text.yview)

root.mainloop()
