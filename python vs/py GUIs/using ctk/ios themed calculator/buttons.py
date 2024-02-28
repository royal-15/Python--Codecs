from customtkinter import CTkButton
from settings import *


class Button(CTkButton):
    def __init__(self, parent, func, text, col, row, font, span=1, color="dark-gray"):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            corner_radius=STYLING["corner-radius"],
            font=font,
            fg_color=COLORS[color]["fg"],
            hover_color=COLORS[color]["hover"],
            text_color=COLORS[color]["text"],
        )
        self.grid(
            column=col,
            row=row,
            sticky="nsew",
            padx=STYLING["gap"],
            pady=STYLING["gap"],
            columnspan=span,
        )


class Num_Button(Button):
    def __init__(self, parent, func, text, col, row, font, span, color="light-gray"):
        super().__init__(
            parent=parent,
            func=lambda: func(text),
            text=text,
            col=col,
            row=row,
            font=font,
            span=span,
            color=color,
        )


class Math_Button(Button):
    def __init__(self, parent, func, text, operator, col, row, font, color="orange"):
        super().__init__(
            parent=parent,
            func=lambda: func(operator),
            text=text,
            col=col,
            row=row,
            font=font,
            color=color,
        )


class Image_Button(CTkButton):
    def __init__(self, parent, func, text, col, row, image, color="dark-gray"):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            image=image,
            corner_radius=STYLING["corner-radius"],
            fg_color=COLORS[color]["fg"],
            hover_color=COLORS[color]["hover"],
            text_color=COLORS[color]["text"],
        )
        self.grid(
            column=col, row=row, sticky="nsew", padx=STYLING["gap"], pady=STYLING["gap"]
        )
