from customtkinter import *
from pannels import *


class Menu(CTkTabview):
    def __init__(self, parent, pos_vars, color_vars, effect_vars, export_image):
        super().__init__(parent)

        self.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

        # tabs
        self.add("Position")
        self.add("Color")
        self.add("Effects")
        self.add("Export")

        # widgets
        PositionFrame(self.tab("Position"), pos_vars)
        ColorFrame(self.tab("Color"), color_vars)
        EffectFrame(self.tab("Effects"), effect_vars)
        ExportFrame(self.tab("Export"), export_image)


class PositionFrame(CTkFrame):
    def __init__(self, parent, pos_vars):
        super().__init__(parent, fg_color="transparent")

        self.pack(expand=TRUE, fill=BOTH)

        SliderPannel(self, "Rotation", pos_vars["rotate"], 0, 360)
        SliderPannel(self, "Zoom", pos_vars["zoom"], 0, 200)
        SegmentPannel(
            self, text="Invert", data_var=pos_vars["flip"], options=FLIP_OPTIONS
        )

        RevertButton(
            self,
            (pos_vars["rotate"], ROTATE_DEFAULT),
            (pos_vars["zoom"], ZOOM_DEFAULT),
            (pos_vars["flip"], FLIP_OPTIONS[0]),
        )


class ColorFrame(CTkFrame):
    def __init__(self, parent, color_vars):
        super().__init__(parent, fg_color="transparent")

        self.pack(expand=TRUE, fill=BOTH)

        SwitchPannel(
            self, (color_vars["grayscale"], "B/W"), (color_vars["invert"], "Invert")
        )
        SliderPannel(self, "Brightness", color_vars["brightness"], 0, 5)
        SliderPannel(self, "Vibrance", color_vars["vibrance"], 0, 5)

        RevertButton(
            self,
            (color_vars["brightness"], BRIGHTNESS_DEFAULT),
            (color_vars["grayscale"], GRAYSCALE_DEFAULT),
            (color_vars["invert"], INVERT_DEFAULT),
            (color_vars["vibrance"], VIBRANCE_DEFAULT),
        )


class EffectFrame(CTkFrame):
    def __init__(self, parent, effect_vars):
        super().__init__(parent, fg_color="transparent")

        self.pack(expand=TRUE, fill=BOTH)

        DropDownPannel(self, effect_vars["effect"], EFFECT_OPTIONS)
        SliderPannel(self, "Blur", effect_vars["blur"], 0, 30)
        SliderPannel(self, "Contrast", effect_vars["contrast"], 0, 3)

        RevertButton(
            self,
            (effect_vars["blur"], BLUR_DEFAULT),
            (effect_vars["contrast"], CONTRAST_DEFAULT),
            (effect_vars["effect"], EFFECT_OPTIONS[0]),
        )


class ExportFrame(CTkFrame):
    def __init__(self, parent, export_image):
        super().__init__(parent, fg_color="transparent")

        self.pack(expand=TRUE, fill=BOTH)

        # data
        self.name_string = StringVar()
        self.file_string = StringVar(value="jpg")
        self.path_string = StringVar()

        # widgets
        FileNamePannel(self, self.name_string, self.file_string)
        FilePathPannel(self, self.path_string)
        SaveButton(
            self, export_image, self.name_string, self.file_string, self.path_string
        )
