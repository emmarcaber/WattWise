import sys
sys.path.append('../')
                           
import login_view
from config.styles import (h1, h2,
                           h3, h4,
                           h5, h6,
                           normal_font, heading_font,
                           style_configurations)

from ttkbootstrap import Style
import ttkbootstrap as ttk
import tkinter as tk


class CreateAccount:

    # Configurations for the main window
    def config_master(self):
        self.master.title("WattWise | Create Account")

        self.window_width = 1100
        self.window_height = 600

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (self.window_width/2))
        y_cordinate = int((screen_height/2) - (self.window_height/2))

        # print(x_cordinate, y_cordinate)
        self.master.geometry("{}x{}+{}+{}".format(self.window_width,
                                                  self.window_height,
                                                  x_cordinate,
                                                  y_cordinate),
                             )

        self.master.minsize(self.window_width, self.window_height)

    def __init__(self, master):
        self.master = master

        self.config_master()
        self.style = Style("litera")
        style_configurations(self)

        self.create_account_frame = ttk.Frame(self.master, padding="30")
        self.create_account_frame.pack(expand=False)

        self.title_label = ttk.Label(self.create_account_frame,
                                     text="WattWise: Kiosk Test Generator and Checker",
                                     style="title_label.TLabel",
                                     )
        self.title_label.grid(row=0,
                              column=0,
                              columnspan=2,
                              sticky="n",
                              pady=(10, 30)
                              )

        self.id_number_label = ttk.Label(
            self.create_account_frame, text="ID Number", style="form_label.TLabel")
        self.first_name_label = ttk.Label(
            self.create_account_frame, text="First Name", style="form_label.TLabel")
        self.last_name_label = ttk.Label(
            self.create_account_frame, text="Last Name", style="form_label.TLabel")
        self.password_label = ttk.Label(
            self.create_account_frame, text="Password", style="form_label.TLabel")

        self.id_number_entry = ttk.Entry(
            self.create_account_frame, font=(heading_font, h5), width=50)
        self.password_entry = ttk.Entry(self.create_account_frame, font=(
            heading_font, h5), width=50, show="*")

        self.create_account_button = ttk.Button(self.create_account_frame,
                                                text="Create Account",
                                                style="success.TButton")
        self.cancel_button = ttk.Button(self.create_account_frame,
                                        text="Cancel",
                                        style="secondary.Outline.TButton",
                                        command=self.cancel_button_clicked
                                        )

        self.id_number_label.grid(
            row=1, column=0, columnspan=2, pady=10, padx=130, sticky="w")
        self.id_number_entry.grid(
            row=2, column=0, columnspan=2, pady=(0, 10), padx=130, sticky="w")
        self.password_label.grid(
            row=4, column=0, columnspan=2, pady=10, padx=130, sticky="w")
        self.password_entry.grid(
            row=5, column=0, columnspan=2, pady=(0, 10), padx=130, sticky="w")
        self.cancel_button.grid(
            row=6, column=0, columnspan=2, pady=(55, 10), padx=128, sticky="w")
        self.create_account_button.grid(
            row=7, column=0, columnspan=2, pady=(10, 10), padx=128, sticky="w")

        self.first_name_label.grid(
            row=3, column=0, pady=10, padx = (130, 0), sticky="w")
        self.last_name_label.grid(
            row=3, column=1, pady=10, sticky="w")

    def cancel_button_clicked(self):
        self.create_account_frame.destroy()

        login_view.Login(self.master)


if __name__ == '__main__':
    root = ttk.Window()
    Login(root)
    root.mainloop()
