import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance

class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.root.title('Image Editor by Rajat')
        self.root.geometry('800x600')
        self.root.configure(bg='black')

        self.canvas = tk.Canvas(self.root, bg='white', bd=0, highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        self.status = tk.Label(self.root, text='Load an image to start editing', bg='black', fg='white', anchor='w')
        self.status.pack(fill='x')

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='Open', command=self.open_image)
        self.file_menu.add_command(label='Save', command=self.save_image)

        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Edit', menu=self.edit_menu)
        self.edit_menu.add_command(label='Rotate', command=self.rotate_image)

        self.image_path = ''
        self.image = None
        self.tk_image = None

    def open_image(self):
        self.image_path = filedialog.askopenfilename()
        self.image = Image.open(self.image_path)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor='nw', image=self.tk_image)
        self.status['text'] = 'Image loaded'

    def save_image(self):
        if self.image:
            self.image.save(self.image_path)
            self.status['text'] = 'Image saved'

    def rotate_image(self):
        if self.image:
            self.image = self.image.rotate(90)
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor='nw', image=self.tk_image)
            self.status['text'] = 'Image rotated'

if __name__ == '__main__':
    root = tk.Tk()
    editor = ImageEditor(root)
    root.mainloop()
