from customtkinter import *
from buttons import Button, Image_Button, Num_Button, Math_Button
import darkdetect
from PIL import Image
from settings import *


class Calculator(CTk):
    def __init__(self, is_dark):
        # Setup
        super().__init__()

        # 2. fg_color  - WHITE or BLACK
        self.configure(fg_color=(WHITE, BLACK))

        # 1. set appearance to dark or light depending on is_dark
        set_appearance_mode(f'{"dark" if is_dark else "light"}')

        # 3. get the start window size from the settings and disable window resizing
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_coordinate = (screen_width // 2) - (APP_SIZE[0] // 2)
        y_coordinate = (screen_height // 2) - (APP_SIZE[1] // 2)

        self.geometry(f"{APP_SIZE[0]}x{APP_SIZE[1]}+4500")
        self.resizable(False, False)

        # 4. hide the title and the icon
        self.title("")
        self.iconbitmap("empty.ico")

        # grid layout
        self.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform="a")
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform="a")

        # data
        self.result_string = StringVar(value="0")
        self.formula_string = StringVar(value="")
        self.display_nums = []
        self.full_operation = []

        # Widgets
        self.create_widgets()

        self.mainloop()

    def create_widgets(self):
        # fonts
        main_font = CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        results_font = CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)

        # output labels
        OutputLabel(self, 0, "se", main_font, self.formula_string)  # formula
        OutputLabel(self, 1, "e", results_font, self.result_string)  # result

        # clear (AC) button
        Button(
            parent=self,
            func=self.clear,
            text=OPERATORS["clear"]["text"],
            col=OPERATORS["clear"]["col"],
            row=OPERATORS["clear"]["row"],
            font=main_font,
        )

        # percentage buttoon
        Button(
            parent=self,
            func=self.percent,
            text=OPERATORS["percent"]["text"],
            col=OPERATORS["percent"]["col"],
            row=OPERATORS["percent"]["row"],
            font=main_font,
        )

        # invert button
        Button(
            parent=self,
            func=self.invert,
            text="+/-",
            col=OPERATORS["invert"]["col"],
            row=OPERATORS["invert"]["row"],
            font=main_font,
        )

        # number buttons
        for num, data in NUM_POSITION.items():
            Num_Button(
                parent=self,
                func=self.num_press,
                text=num,
                col=data["col"],
                row=data["row"],
                font=main_font,
                span=data["span"],
            )

        # math buttons
        for operator, data in MATH_POSITIONS.items():
            Math_Button(
                parent=self,
                func=self.math_press,
                text=data["character"],
                operator=operator,
                col=data["col"],
                row=data["row"],
                font=main_font,
            )

        _ = """resized_light_image = self.resize_images(
            OPERATORS["invert"]["image-path"]["dark"], (600, 600)
        )
        resized_dark_image = self.resize_images(
            OPERATORS["invert"]["image-path"]["light"], (600, 600)
        )
        invert_images = CTkImage(
            resized_light_image,
            resized_dark_image,
        )
        Image_Button(
            parent=self,
            text="",
            func=self.invert,
            col=OPERATORS["invert"]["col"],
            row=OPERATORS["invert"]["row"],
            image=invert_images,
        )"""

    def num_press(self, value):
        self.display_nums.append(str(value))
        full_num = "".join(self.display_nums)
        self.result_string.set(full_num)

    def math_press(self, value):
        current_number = "".join(self.display_nums)

        if current_number:
            self.full_operation.append(current_number)

            if value != "=":
                # update data
                self.full_operation.append(value)
                self.display_nums.clear()

                # update output
                self.result_string.set("")
                self.formula_string.set(" ".join(self.full_operation))

            else:
                formula = " ".join(self.full_operation)
                result = eval(formula)

                # format the result
                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 3)

                # update data
                self.full_operation.clear()
                self.display_nums = str(result)

                # update the output
                self.result_string.set(result)
                self.formula_string.set(formula)

    def invert(self):
        current_number = "".join(self.display_nums)
        if current_number:
            # positive or negative
            if float(current_number) > 0:
                self.display_nums.insert(0, "-")
            else:
                del self.display_nums[0]

            self.result_string.set("".join(self.display_nums))

    def clear(self):
        # clear the output
        self.result_string.set(0)
        self.formula_string.set("")

        # clear the data
        self.display_nums.clear()
        self.full_operation.clear()

    def percent(self):
        if self.display_nums:
            # get the percentage number
            current_number = float("".join(self.display_nums))
            percent_number = current_number / 100

            # update the data and output
            self.display_nums = list(str(percent_number))
            self.result_string.set(str("".join(self.display_nums)))

    def resize_images(self, path, newsize):
        image = Image.open(rf"{path}")

        width, height = image.size

        # Setting the points for cropped image
        left = 4
        top = height / 5
        right = 154
        bottom = 3 * height / 5

        # Cropped images of above dimension
        croped_image = image.crop((left, top, right, bottom))

        # resizing images
        resized_image = croped_image.resize(newsize)

        return resized_image


class OutputLabel(CTkLabel):
    def __init__(self, parent, row, position, font, string_var):
        super().__init__(parent, font=font, textvariable=string_var)
        self.grid(column=0, columnspan=4, row=row, sticky=position, padx=10)


if __name__ == "__main__":
    Calculator(darkdetect.isDark())
