import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image

# Heading Font Sizes
h1_fs = 39
h2_fs = 31
h3_fs = 25
h4_fs = 20
h5_fs = 16
h6_fs = 13

heading_font = 'Arial'
normal_font = 'Century Gothic'


class LoginFrame(ttk.Frame):
    def style_configurations(self):
        styles = ttk.Style()
        styles.configure("id_number_label.TLabel",
                         foreground='black', font=(normal_font, h5_fs))
        styles.configure("primary.TButton", font=(
            normal_font, h5_fs), width=50, padding=10)
        styles.configure("primary.Outline.TButton", font=(
            normal_font, h5_fs), width=50, padding=10)

    def __init__(self, master):
        super().__init__(master)

        self.style_configurations()
        self.configure(padding=(170, 0))

        self.id_number_label = ttk.Label(
            master=self, text="ID Number", style="id_number_label.TLabel")
        self.password_label = ttk.Label(
            master=self, text="Password", style="id_number_label.TLabel")

        self.id_number_entry = ttk.Entry(
            master=self, font=(heading_font, h5_fs), width=50)
        self.password_entry = ttk.Entry(master=self, font=(
            heading_font, h5_fs), width=50, show="*")

        self.login_button = ttk.Button(
            master=self, text="Login", style="primary.TButton")
        self.create_account_button = ttk.Button(
            master=self, text="Create Account", style="primary.Outline.TButton")

        self.id_number_label.grid(
            row=0, column=0, columnspan=2, pady=10, sticky=W)
        self.id_number_entry.grid(
            row=1, column=0, columnspan=2, pady=(0, 10), sticky=W)
        self.password_label.grid(
            row=2, column=0, columnspan=2, pady=10, sticky=W)
        self.password_entry.grid(
            row=3, column=0, columnspan=2, pady=(0, 10), sticky=W)
        self.login_button.grid(
            row=4, column=0, columnspan=2, pady=(55, 10), sticky="w")
        self.create_account_button.grid(
            row=5, column=0, columnspan=2, pady=(10, 10), sticky="w")


class LoginWindow(ttk.Window):

    def style_configurations(self):
        styles = ttk.Style()
        styles.configure('title_label.TLabel', font=(heading_font, h3_fs))

    def __init__(self):
        super().__init__()

        self.title("WattWise")
        self.open_in_center_screen()
        self.style_configurations()

        # self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1), weight=1)

        self.add_components()

    def add_components(self):
        img = tk.PhotoImage(file="logo.png")
        self.title_label = ttk.Label(
            self, text="WattWise : Kiosk Test Generator and Checker", style="title_label.TLabel", justify="center")
        self.title_label.grid(row=0, column=0, columnspan=2,
                              padx=20, pady=(70, 40), sticky=N)

        self.login_frame = LoginFrame(self)
        self.login_frame.grid(row=1, column=0, sticky=NSEW)

    def open_in_center_screen(self):
        self.window_width = 1100
        self.window_height = 700

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (self.window_width/2))
        y_cordinate = int((screen_height/2) - (self.window_height/2))

        # print(x_cordinate, y_cordinate)
        self.geometry("{}x{}+{}+{}".format(self.window_width,
                                           self.window_height, x_cordinate, y_cordinate))

        self.minsize(self.window_width, self.window_height)


if __name__ == '__main__':
    app = LoginWindow()
    app.mainloop()
