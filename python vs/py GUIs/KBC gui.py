from tkinter import *
import ttkbootstrap as tb
from tkinter import messagebox as msg

questions = [
    [
        "Which is the single largest internal organ by mass in the human body?",
        "Liver",
        "Gallbladder",
        "Kidney",
        "Stomach",
        1,
    ],
    [
        "Which of these is a non-renewable source of energy?",
        "Solar power",
        "Hydro power",
        "Wind power",
        "Natural gas",
        4,
    ],
    [
        "Which of these does the carpenter use to smoothen the surface of a wooden furniture?",
        "Butter paper",
        "Silver paper",
        "Tissue paper",
        "Sandpaper",
        4,
    ],
    [
        "A video clip from Manikarnika: The Queen of Jhansi, starring Kangana Ranaut was shown?",
        "Jhansi",
        "Gwalior",
        "Jaipur",
        "Varanasi",
        4,
    ],
    [
        "Besides Sachin Tendulkar, who is the only other Indian cricketer to have scored over 13,000 runs in test cricket?",
        "Virat Kohli",
        "Sunil Gavaskar",
        "VVS laxman",
        "Rahul Dravid",
        1,
    ],
    [
        "Ranthambore, Sariska and Keoladeo Ghana are all names of what?",
        "National Parks",
        "Goosebumps",
        "Mountains",
        "Rivers",
        1,
    ],
    [
        "India's official entry to Oscars 2021, ” Jallikattu ” is, a film in which language?",
        "Hindi",
        "Punjabi",
        "Kannada",
        "Malayalam",
        4,
    ],
    [
        "Which of the following companies was originally started as a loom manufacturing unit in 1909?",
        "Suzuki",
        "CEAT",
        "Honda",
        "Mercedes",
        1,
    ],
    [
        "What is the profession of Kabir in the film Kabir Singh?",
        "Engineer",
        "Cricketor",
        "Athlete",
        "Doctor",
        4,
    ],
    [
        "Which state is the largest producer of sugarcane in India?",
        "Maharashtra",
        "Karnataka",
        "Madhya Pradesh",
        "Uttar Pradesh",
        4,
    ],
    [
        "Which of these colors when mixed with red will produce the color orange?",
        "Violet",
        "Green",
        "Orange",
        "Yellow",
        4,
    ],
    [
        "Which part of the plant absorbs water and nutrients from the soil?",
        "Stem",
        "Buds",
        "Leafs",
        "Root",
        4,
    ],
    [
        "Who of the following personalities is not married to a sports person?",
        "Anushka Sharma",
        "Sakshi Singh Rawat",
        "Mahesh Bhupathi",
        "Sharmila Tagore",
        3,
    ],
    [
        "Jafdarabadi, Surti, Neely Ravi, Bhadavari, Nagpuri, Mehsana and Toda are all of the breeds of which animal?",
        "Cow",
        "Hen",
        "Goat",
        "Buffalo",
        4,
    ],
    [
        "Which ingredient is mixed in milk is a popular home remedy for healing any internal injury?",
        "Lemon",
        "Honey",
        "Almond",
        "Turmeric",
        4,
    ],
]
answers = [
    "Liver",
    "Natural gas",
    "Sandpaper",
    "Varanasi",
    "Virat Kohli",
    "National Parks",
    "Malayalam",
    "Suzuki",
    "Doctor",
    "Uttar Pradesh",
    "Yellow",
    "Root",
    "Mahesh Bhupathi",
    "Buffalo",
    "Turmeric",
]
levels = [
    " ₹ 1,000",
    " ₹ 2,000",
    " ₹ 3,000",
    " ₹ 5,000",
    " ₹ 10,000",
    " ₹ 20,000",
    " ₹ 40,000",
    " ₹ 80,000",
    " ₹ 160,000",
    " ₹ 320,000",
    " ₹ 640,000",
    " ₹ 1,250,000",
    " ₹ 5,000,000",
    " ₹ 1 crore",
    " ₹ 7 crore",
]


def _help():
    guide_text = """KBC game:
    author: Rajat Sharma
    publisher: Rajat Sharma"""
    msg.showinfo("Guide", guide_text)


class main_window(tb.Window):
    def __init__(self):
        super().__init__()
        self.geometry("650x500")
        self.minsize(650, 500)
        self.title("KBC game")

        # start window
        self.startwindow = self.start_window()
        self.startwindow.pack(expand=TRUE, fill=BOTH)

        self.mainloop()

    def start_window(self):
        frame = tb.Frame(self)

        # widgets
        wlcome_label = tb.Label(frame, text="Welcome To KBC", font="classic 30 bold")
        start_button = tb.Button(frame, text="Start Game", command=self.start)

        # layout
        wlcome_label.pack(pady=60)
        start_button.pack(pady=40)

        return frame

    def end_window(self):
        frame = tb.Frame(self)

        # widgets
        game_over_label = tb.Label(frame, text="Game Over!!", font="classic 30 bold")
        self.score_label = tb.Label(frame, text="Total Score:", font="classic 20 bold")
        self.restart_button = tb.Button(
            frame, text="Restart Game", command=self.restart
        )

        # layout
        game_over_label.pack(pady=40)
        self.score_label.pack(pady=30)
        self.restart_button.pack(pady=30)

        return frame

    def restart(self):
        pass

    def start(self):
        self.startwindow.pack_forget()
        # middle window
        middlewindow = middle_window(self)


# parent - main_window
class middle_window(tb.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # rows & column configuration
        self.rowconfigure(0, weight=20)
        self.rowconfigure(1, weight=50)
        self.rowconfigure(2, weight=30)
        self.columnconfigure(0, weight=1)

        # wait variable
        self.button_pressed = BooleanVar(value=FALSE)

        # won money
        self.money = "₹ 0"

        # layout
        for i in range(len(questions)):
            self.f1 = frame1(self, levels[i])
            self.f2 = frame2(self, questions[i][0])
            self.f3 = frame3(
                self, questions[i][1], questions[i][2], questions[i][3], questions[i][4]
            )

            # binding events to buttons
            self.f1.quit_button.bind("<Button-1>", lambda event: self.quit(i))
            self.f3.Abutton.bind("<Button-1>", lambda event: self.button(event, i))
            self.f3.Bbutton.bind("<Button-1>", lambda event: self.button(event, i))
            self.f3.Cbutton.bind("<Button-1>", lambda event: self.button(event, i))
            self.f3.Dbutton.bind("<Button-1>", lambda event: self.button(event, i))

            self.wait_variable(self.button_pressed)

        self.pack(expand=TRUE, fill=BOTH)

    def button(self, event, i):
        self.button_pressed.set(TRUE)
        text = event.widget.cget("text")
        if text in answers:
            msg.showinfo(
                "correct answer (✔)",
                f"""       congratulation\n  You have won {levels[i]}""",
            )
            if i - 1 == 4:
                self.money = levels[4]
            elif i - 1 == 9:
                self.money = levels[9]
            elif i - 1 == 14:
                self.money = levels[14]
        else:
            if i < 4:
                self.money = "₹ 0"
            msg.showinfo(
                "Wrong answer (✘)", f"Now your total winings are downto {self.money}"
            )

    def quit(self, i):
        if i > 0:
            self.money = levels[i - 1]
            msg.showinfo(
                "Quited", f"You quited the game and your total winings are {self.money}"
            )
        else:
            msg.showwarning("Idiot", "Go and develop your brain..")

        self.destroy()


# leveltext
class frame1(tb.Frame):
    def __init__(self, parent, leveltext):
        super().__init__(parent)

        # widgets
        help_button = tb.Button(self, text="?", command=_help)
        level_label = tb.Label(self, text=leveltext, font="classic 16 bold")
        self.quit_button = tb.Button(self, text="Quit", command=quit)

        # layout
        help_button.place(relx=0.08, rely=0.2)
        level_label.place(relx=0.18, rely=0.2)
        self.quit_button.place(relx=0.92, rely=0.2, anchor="ne")

        self.grid(row=0, column=0, sticky="nsew")


# questiontext, wl
class frame2(tb.Frame):
    def __init__(self, parent, questiontext):
        super().__init__(parent)

        # wrap length
        initial_wrap_length = self.winfo_width() // 2

        # widgets
        Q_label = tb.Label(self, text="Q.", font="classic 27 bold")
        question_label = tb.Label(
            self,
            text=questiontext,
            font="classic 20 bold",
            wraplength=initial_wrap_length,
        )
        self.won_label = tb.Label(self, text=f"Won: ", font="classic 16 bold")

        # layout
        Q_label.place(relx=0.06, rely=0.2)
        question_label.place(relx=0.17, rely=0.23)
        self.won_label.place(relx=0.9, rely=0.9, anchor="se")

        self.grid(row=1, column=0, sticky="nsew")


# Abuttontext, Bbuttontext, Cbuttontext, Dbuttontext
class frame3(tb.Frame):
    def __init__(self, parent, Abuttontext, Bbuttontext, Cbuttontext, Dbuttontext):
        super().__init__(parent)

        # configuration
        self.rowconfigure(0, weight=20)
        self.rowconfigure(1, weight=25)
        self.rowconfigure(2, weight=10)
        self.rowconfigure(3, weight=25)
        self.rowconfigure(4, weight=20)

        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=8)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=25)
        self.columnconfigure(4, weight=15)
        self.columnconfigure(5, weight=8)
        self.columnconfigure(6, weight=2)
        self.columnconfigure(7, weight=25)
        self.columnconfigure(8, weight=15)

        # widgets
        Alabel = tb.Label(self, text="A.", font="classic 25 bold")
        Blabel = tb.Label(self, text="B.", font="classic 25 bold")
        Clabel = tb.Label(self, text="C.", font="classic 25 bold")
        Dlabel = tb.Label(self, text="D.", font="classic 25 bold")

        self.Abutton = tb.Button(self, text=Abuttontext)
        self.Bbutton = tb.Button(self, text=Bbuttontext)
        self.Cbutton = tb.Button(self, text=Cbuttontext)
        self.Dbutton = tb.Button(self, text=Dbuttontext)

        # layout
        Alabel.grid(row=1, column=1, sticky="nsew")
        self.Abutton.grid(row=1, column=3, sticky="nsew")

        Blabel.grid(row=1, column=5, sticky="nsew")
        self.Bbutton.grid(row=1, column=7, sticky="nsew")

        Clabel.grid(row=3, column=1, sticky="nsew")
        self.Cbutton.grid(row=3, column=3, sticky="nsew")

        Dlabel.grid(row=3, column=5, sticky="nsew")
        self.Dbutton.grid(row=3, column=7, sticky="nsew")

        self.grid(row=2, column=0, sticky="nsew")


# main program
window = main_window()
