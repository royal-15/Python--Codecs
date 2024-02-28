from customtkinter import *
from screeninfo import get_monitors as gm
from tkinter import font, messagebox
import requests as rq


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.minsize(500, 400)
        self.maxsize(500, 400)
        self.title("Image Downloader")
        self.configure(padx=20)

        # print(font.families())

        # Main Heading
        CTkLabel(self, text="Image Downloader By Rajat", font=("Death Note", 40)).pack(
            pady=25
        )

        # Entries Frame
        self.entries_frame = self.create_entries()
        self.entries_frame.pack(pady=20, expand=TRUE, fill=BOTH)

        # Download Buttons
        self.download_buttons_frame = self.download_buttons()
        self.download_buttons_frame.pack(pady=10)

        if self.random_tick.get():
            self.url_entry.configure(state=DISABLED)
            self.entries_frame.update()
        else:
            self.url_entry.configure(state=NORMAL)
            self.entries_frame.update()

        # Status Label
        self.status_label = CTkLabel(self, text="Status:", font=("Merriweather", 14))
        self.status_label.pack(pady=20)

        self.mainloop()

    def create_entries(self):
        frame = CTkFrame(self, height=1000)
        formats = [".png", ".jpg", ".jpeg", ".json"]

        # Frame Configuration
        frame.columnconfigure((0, 1, 2), weight=1, uniform="a")
        frame.rowconfigure((0, 1), weight=1, uniform="a")

        # Widgets
        font_name = "Merriweather"
        font_size = 18
        url_label = CTkLabel(
            frame, text="Image URL :", font=(font_name, font_size, "bold")
        )
        self.url_entry = CTkEntry(
            frame, font=("consolas", 14), placeholder_text="image url here.."
        )
        name_label = CTkLabel(
            frame, text="Image Name :", font=(font_name, font_size, "bold")
        )
        self.name_entry = CTkEntry(
            frame, font=("consolas", 14), placeholder_text="image name here.."
        )
        self.formats_box = CTkComboBox(frame, values=formats, font=("classic", 18))

        # layout
        url_label.grid(row=0, column=0, sticky="ew")
        self.url_entry.grid(row=0, column=1, columnspan=2, sticky="ew")
        name_label.grid(row=1, column=0, sticky="ew")
        self.name_entry.grid(row=1, column=1, sticky="w")
        self.formats_box.grid(row=1, column=2, sticky="e")

        return frame

    def download_buttons(self):
        frame = CTkFrame(self)

        hwfont = ("Merriweather", 14, "bold")

        # Widgets
        self.random_tick = CTkCheckBox(
            frame,
            text="Random url",
            onvalue=TRUE,
            offvalue=FALSE,
            font=("Merriweather", 10),
        )
        self.width_entry = CTkEntry(
            frame, placeholder_text="width", font=hwfont, width=100
        )
        label = CTkLabel(frame, text="x", font=("Merriweather", 12))
        self.height_entry = CTkEntry(
            frame, placeholder_text="height", font=hwfont, width=100
        )
        self.download_button = CTkButton(
            frame,
            text="Download",
            command=self.download,
            font=("Merriweather", 16),
        )

        # Layout
        self.width_entry.pack(side=LEFT)
        label.pack(side=LEFT)
        self.height_entry.pack(side=LEFT)
        self.random_tick.pack(side=LEFT)
        self.download_button.pack(side=RIGHT)
        # tt(self.download_button, "click to download file for provided url")

        return frame

    def update_buttons_layout(self):
        pass

    def download(self):
        if self.random_tick.get():
            self.status_label.configure(text=f"Searching for Image & Downloading...")
            self.status_label.update()

            if self.width_entry.get() == "" or self.height_entry.get() == "":
                width = gm()[0].width
                height = gm()[0].height
            else:
                try:
                    width = int(self.width_entry.get())
                    height = int(self.heigth_entry.get())
                    # print(width, height)
                except:
                    messagebox.showwarning(
                        "Invalid Height / Width!!!",
                        "Got Invalid Height / Width, Using Default Height & Width to Continue",
                    )
                    width = gm()[0].width
                    height = gm()[0].height

            url = f"https://picsum.photos/{width}/{height}"

            r = rq.get(url)

            if self.name_entry.get() == "":
                savename = "new" + self.formats_box.get()
            else:
                savename = self.name_entry.get() + self.formats_box.get()

            with open(savename, "wb") as f:
                f.write(r.content)

            self.status_label.configure(text=f"Downloaded file as {savename}")
        else:
            try:
                self.status_label.configure(text=f"Image Downloading...")
                self.status_label.update()

                url = self.url_entry.get()

                r = rq.get(url)

                if self.name_entry.get() == "":
                    savename = "new" + self.formats_box.get()
                else:
                    savename = self.name_entry.get() + self.formats_box.get()

                with open(savename, "wb") as f:
                    f.write(r.content)

                self.status_label.configure(text=f"Downloaded Image as {savename}")
            except:
                self.status_label.configure(text=f"Download Failed!!!")
                self.status_label.update()
                messagebox.showerror(
                    "Download Failed!!!",
                    'Please "Check Your URL" it might be expired or incorrect',
                )
                self.status_label.configure(text=f"Status:")
                self.status_label.update()


MainWindow()
