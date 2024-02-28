from customtkinter import *
from settings import *

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


class App(CTk):
    def __init__(self):
        super().__init__(fg_color=GREEN)
        self.geometry("400x400")
        self.resizable(False, False)
        self.title("")

        # Layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")

        # Data
        self.metric_boolean = BooleanVar(value=TRUE)
        self.height_int = IntVar(value=170)
        self.weight_float = DoubleVar(value=65)
        self.bmi_string = StringVar()
        self.update_bmi()

        # Tracing
        self.height_int.trace("w", self.update_bmi)
        self.weight_float.trace("w", self.update_bmi)
        self.metric_boolean.trace("w", self.change_units)

        # Widgets
        ResultText(self, self.bmi_string)
        self.weight_input = WeightInput(self, self.weight_float, self.metric_boolean)
        self.height_input = HeightInput(self, self.height_int, self.metric_boolean)
        UnitSwitcher(self, self.metric_boolean)

        self.mainloop()

    def change_units(self, *args):
        self.height_input.update_text(self.height_int.get())
        self.weight_input.update_weight()

    def update_bmi(self, *args):
        height_meter = self.height_int.get() / 100
        weight_kg = self.weight_float.get()
        bmi_result = round(weight_kg / height_meter**2, 2)
        self.bmi_string.set(bmi_result)

    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_HEX_COLOR
            windll.dwmapi.DwmSetWindowAttribute(
                HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int)
            )
        except:
            pass


class ResultText(CTkLabel):
    def __init__(self, parent, bmi_string):
        font = CTkFont(family=FONT, size=MAIN_TEXT_SIZE, weight="bold")
        super().__init__(
            parent, text=22.5, font=font, text_color=WHITE, textvariable=bmi_string
        )

        self.grid(column=0, row=0, rowspan=2, sticky="nsew")


class WeightInput(CTkFrame):
    def __init__(self, parent, weight_float, metric_boolean):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(column=0, row=2, sticky="nsew", padx=10, pady=10)
        self.weight_float = weight_float
        self.metric_boolean = metric_boolean

        # Layout
        self.rowconfigure(0, weight=1, uniform="b")
        self.columnconfigure(0, weight=2, uniform="b")
        self.columnconfigure(1, weight=1, uniform="b")
        self.columnconfigure(2, weight=3, uniform="b")
        self.columnconfigure(3, weight=1, uniform="b")
        self.columnconfigure(4, weight=2, uniform="b")

        # Text Variable
        self.output_string = StringVar()
        self.update_weight()

        # Output Label
        font = CTkFont(family=FONT, size=INPUT_FONT_SIZE)
        label = CTkLabel(self, text_color=BLACK, textvariable=self.output_string)
        label.grid(row=0, column=2)

        # Buttons
        minus_button = CTkButton(
            self,
            text="-",
            font=font,
            text_color=BLACK,
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            corner_radius=BUTTON_CORNOR_RADIUS,
            command=lambda: self.update_weight(("minus", "large")),
        )
        minus_button.grid(row=0, column=0, sticky="ns", padx=8, pady=8)

        plus_button = CTkButton(
            self,
            text="+",
            font=font,
            text_color=BLACK,
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            corner_radius=BUTTON_CORNOR_RADIUS,
            command=lambda: self.update_weight(("plus", "large")),
        )
        plus_button.grid(row=0, column=4, sticky="ns", padx=8, pady=8)

        small_plus_button = CTkButton(
            self,
            text="+",
            font=font,
            text_color=BLACK,
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            corner_radius=BUTTON_CORNOR_RADIUS,
            command=lambda: self.update_weight(("plus", "small")),
        )
        small_plus_button.grid(row=0, column=3, padx=4, pady=4)

        small_minus_button = CTkButton(
            self,
            text="-",
            font=font,
            text_color=BLACK,
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            corner_radius=BUTTON_CORNOR_RADIUS,
            command=lambda: self.update_weight(("minus", "small")),
        )
        small_minus_button.grid(row=0, column=1, padx=4, pady=4)

    def update_weight(self, info=None):
        if info:
            if self.metric_boolean.get():
                amount = 1 if info[1] == "large" else 0.1
            else:
                amount = 0.453592 if info[1] == "large" else 0.453591 / 16
                # ponds
                # ounces
                pass

            if info[0] == "plus":
                self.weight_float.set(self.weight_float.get() + amount)
            else:
                self.weight_float.set(self.weight_float.get() - amount)

        if self.metric_boolean.get():
            self.output_string.set(f"{round(self.weight_float.get(), 1)}kg")
        else:
            raw_ounces = self.weight_float.get() * 2.20462
            pounds, ounces = divmod(raw_ounces, 16)
            self.output_string.set(f"{int(pounds)}lb {round(ounces, 2)}oz")


class HeightInput(CTkFrame):
    def __init__(self, parent, height_int, metric_boolean):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
        self.metric_boolean = metric_boolean

        # Widgets
        slider = CTkSlider(
            self,
            command=self.update_text,
            button_color=GREEN,
            button_hover_color=GRAY,
            progress_color=GREEN,
            fg_color=LIGHT_GRAY,
            variable=height_int,
            from_=100,
            to=250,
        )
        slider.pack(side=LEFT, fill=X, expand=True, pady=10, padx=10)

        self.output_string = StringVar()
        self.update_text(height_int.get())

        output_text = CTkLabel(
            self,
            text_color=BLACK,
            font=CTkFont(family=FONT, size=INPUT_FONT_SIZE),
            textvariable=self.output_string,
        )
        output_text.pack(side=LEFT, padx=20)

    def update_text(self, amount):
        if self.metric_boolean.get():  # for metric units
            text_string = str(int(amount))
            meter = text_string[0]
            cm = text_string[1:]
            self.output_string.set(f"{meter}.{cm}m")
        else:  # for imperial units
            feet, inches = divmod(amount / 2.54, 12)
            self.output_string.set(f"{int(feet)}'{int(inches)}\"")


class UnitSwitcher(CTkLabel):
    def __init__(self, parent, metric_boolean):
        super().__init__(
            parent,
            text="metric",
            text_color=DARK_GREEN,
            font=CTkFont(family=FONT, size=SWITCH_FONT_SIZE, weight="bold"),
        )
        self.place(relx=0.98, rely=0.01, anchor="ne")

        self.metric_boolean = metric_boolean
        self.bind("<Button>", self.change_units)

    def change_units(self, event):
        self.metric_boolean.set(not self.metric_boolean.get())

        if self.metric_boolean.get():
            self.configure(text="Metric")
        else:
            self.configure(text="Imperial")


if __name__ == "__main__":
    app = App()
