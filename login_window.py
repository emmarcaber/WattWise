import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image


class App(ttk.Window):

    # Style Configurations
    def style_configurations(self):
        styles = ttk.Style()
        styles.configure('title_label.TLabel', font=("Century Gothic", 24))

    def __init__(self):
        super().__init__()

        self.style_configurations()

        self.title("WattWise")
        self.open_in_center_screen()

        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        img = tk.PhotoImage(file="logo.png")
        self.title_label = ttk.Label(
            self, text="WattWise : Kiosk Test Generator and Checker", style="title_label.TLabel", justify="center")
        self.title_label.grid(row=0, column=0, columnspan=2,
                              padx=20, pady=20, sticky=N)
    

    def open_in_center_screen(self):
        self.window_width = 1100
        self.window_height = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (self.window_width/2))
        y_cordinate = int((screen_height/2) - (self.window_height/2))

        print(x_cordinate, y_cordinate)
        self.geometry("{}x{}+{}+{}".format(self.window_width,
                                           self.window_height, x_cordinate, y_cordinate))

        self.minsize(self.window_width, self.window_height)


if __name__ == '__main__':
    app = App()
    app.mainloop()
