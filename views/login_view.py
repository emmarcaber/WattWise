import sys
import create_account_view
from config.styles import (h1, h2,
                           h3, h4,
                           h5, h6,
                           normal_font, heading_font,
                           style_configurations)

from ttkbootstrap import Style
import ttkbootstrap as ttk
import tkinter as tk

sys.path.append('../')


class Login:

    # Configurations for the main window
    def config_master(self):
        self.master.title("WattWise | Login")

        self.window_width = 1100
        self.window_height = 600

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (self.window_width / 2))
        y_coordinate = int((screen_height / 2) - (self.window_height / 2))

        self.master.geometry("{}x{}+{}+{}".format(self.window_width,
                                                  self.window_height,
                                                  x_coordinate,
                                                  y_coordinate),
                             )

        self.master.minsize(self.window_width, self.window_height)

    def __init__(self, master):
        self.master = master

        self.config_master()
        self.style = Style("litera")
        style_configurations(self)

        self.login_frame = ttk.Frame(self.master, padding="30")
        self.login_frame.pack(expand=False)

        self.title_label = ttk.Label(self.login_frame,
                                     text="WattWise: Kiosk Test Generator and Checker",
                                     style="title_label.TLabel",
                                     )
        self.title_label.grid(row=0,
                              column=1,
                              columnspan=2,
                              sticky="n",
                              pady=(10, 30)
                              )

        self.id_number_label = ttk.Label(
            self.login_frame, text="ID Number", style="form_label.TLabel")
        self.first_name_label = ttk.Label(
            self.login_frame, text="First Name", style="form_label.TLabel")
        self.last_name_label = ttk.Label(
            self.login_frame, text="Last Name", style="form_label.TLabel")
        self.password_label = ttk.Label(
            self.login_frame, text="Password", style="form_label.TLabel")

        self.id_number_entry = ttk.Entry(
            self.login_frame, font=(heading_font, h5), width=50)
        self.password_entry = ttk.Entry(self.login_frame, font=(
            heading_font, h5), width=50, show="*")

        self.login_button = ttk.Button(
            self.login_frame, text="Login", style="login_button.TButton")
        self.create_account_button = ttk.Button(self.login_frame,
                                                text="Create Account",
                                                style="create_account_button.Outline.TButton",
                                                command=self.create_account_clicked)

        self.id_number_label.grid(
            row=1, column=0, columnspan=2, pady=10, padx=130, sticky="w")
        self.id_number_entry.grid(
            row=3, column=0, columnspan=2, pady=(0, 10), padx=130, sticky="w")
        self.password_label.grid(
            row=4, column=0, columnspan=2, pady=10, padx=130, sticky="w")
        self.password_entry.grid(
            row=5, column=0, columnspan=2, pady=(0, 10), padx=130, sticky="w")
        self.login_button.grid(
            row=6, column=0, columnspan=2, pady=(55, 10), padx=128, sticky="w")
        self.create_account_button.grid(
            row=7, column=0, columnspan=2, pady=(10, 10), padx=128, sticky="w")

    def create_account_clicked(self):
        self.login_frame.destroy()

        create_account_view.CreateAccount(self.master)


if __name__ == '__main__':
    root = ttk.Window()
    Login(root)
    root.mainloop()
