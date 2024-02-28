from customtkinter import *
from tkinter import filedialog
from settings import *


class Pannel(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=DARK_GREY)

        self.pack(fill="x", pady=4, ipady=8)


class SliderPannel(Pannel):
    def __init__(self, parent, text, data_var, min_value, max_value):
        super().__init__(parent)

        # layout
        self.rowconfigure(
            (0, 1),
            weight=1,
        )
        self.columnconfigure(
            (0, 1),
            weight=1,
        )

        self.data_var = data_var
        self.data_var.trace("w", self.update_text)

        CTkLabel(self, text=text).grid(column=0, row=0, sticky="w", padx=5)

        self.num_label = CTkLabel(self, text=data_var.get())
        self.num_label.grid(column=1, row=0, sticky="e", padx=5)

        CTkSlider(
            self,
            fg_color=SLIDER_BG,
            variable=self.data_var,
            from_=min_value,
            to=max_value,
        ).grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    def update_text(self, *args):
        self.num_label.configure(text=f"{round(self.data_var.get(), 2)}")


class SegmentPannel(Pannel):
    def __init__(self, parent, text, data_var, options):
        super().__init__(parent)

        CTkLabel(self, text=text).pack()
        CTkSegmentedButton(self, variable=data_var, values=options).pack(
            expand=TRUE, fill=BOTH, padx=4, pady=4
        )


class SwitchPannel(Pannel):
    def __init__(self, parent, *args):  # ((var, text), (var, text), (var, text),)
        super().__init__(parent)

        for var, text in args:
            switch = CTkSwitch(
                self, text=text, variable=var, button_color=BLUE, fg_color=SLIDER_BG
            )
            switch.pack(side=LEFT, expand=TRUE, fill=BOTH, padx=5, pady=5)


class FileNamePannel(Pannel):
    def __init__(self, parent, name_string, file_string):
        super().__init__(parent)

        # data
        self.name_string = name_string
        self.name_string.trace("w", self.update_text)
        self.file_string = file_string

        # check boxesf for file formate
        CTkEntry(self, textvariable=self.name_string).pack(fill="x", padx=20, pady=5)
        frame = CTkFrame(self, fg_color="transparent")

        jpg_check = CTkCheckBox(
            frame,
            text="jpg",
            variable=self.file_string,
            command=lambda: self.click("jpg"),
            onvalue="jpg",
            offvalue="png",
        )
        png_check = CTkCheckBox(
            frame,
            text="png",
            variable=self.file_string,
            command=lambda: self.click("png"),
            onvalue="png",
            offvalue="jpg",
        )

        jpg_check.pack(side=LEFT, fill=X, expand=TRUE)
        png_check.pack(side=LEFT, fill=X, expand=TRUE)

        frame.pack(expand=TRUE, fill=X, padx=20, pady=5)

        # preview text
        self.output = CTkLabel(self, text="")
        self.output.pack()

    def update_text(self, *args):
        if self.name_string.get():
            text = (
                self.name_string.get().replace(" ", "_") + "." + self.file_string.get()
            )
            self.output.configure(text=text)

    def click(self, value):
        self.file_string.set(value)
        self.update_text()


class FilePathPannel(Pannel):
    def __init__(self, parent, path_string):
        super().__init__(parent)
        self.path_string = path_string

        CTkButton(self, text="Open Explorer", command=self.open_file_dialog).pack(
            pady=5
        )
        CTkEntry(self, textvariable=self.path_string).pack(
            expand=True, fill=BOTH, padx=5, pady=5
        )

    def open_file_dialog(self):
        self.path_string.set(filedialog.askdirectory())


class DropDownPannel(CTkOptionMenu):
    def __init__(self, parent, data_var, options):
        super().__init__(
            master=parent,
            values=options,
            fg_color=DARK_GREY,
            button_color=DROPDOWN_MAIN_COLOR,
            button_hover_color=DROPDOWN_HOVER_COLOR,
            dropdown_fg_color=DROPDOWN_MENU_COLOR,
            variable=data_var,
        )
        self.pack(fill="x", pady=4)


class RevertButton(CTkButton):
    def __init__(self, parent, *args):
        super().__init__(parent, text="Revert", command=self.revert)

        self.pack(side=BOTTOM, pady=10)

        self.args = args

    def revert(self):
        for var, value in self.args:
            var.set(value)


class SaveButton(CTkButton):
    def __init__(self, parent, export_image, name_string, file_string, path_string):
        super().__init__(parent, text="Save", command=self.save)
        self.pack(side=BOTTOM, pady=10)

        self.export_image = export_image
        self.name_string = name_string
        self.file_string = file_string
        self.path_string = path_string

    def save(self):
        self.export_image(
            self.name_string.get(),
            self.file_string.get(),
            self.path_string.get(),
        )
