# Window for Creating User Accounts

import sys
from tkinter import messagebox

import login_view
from models import user_model
import ttkbootstrap as ttk
from ttkbootstrap import Style
from config.styles import (h5, heading_font,
                           style_configurations)

sys.path.append('../')


class CreateAccount:

    # Configurations for the main window
    def config_master(self):
        self.master.title("WattWise | Create Account")

        self.window_width = 1100
        self.window_height = 680

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x_coordinate = int((screen_width/2) - (self.window_width/2))
        y_coordinate = int((screen_height/2) - (self.window_height/2))

        self.master.geometry("{}x{}+{}+{}".format(self.window_width,
                                                  self.window_height,
                                                  x_coordinate,
                                                  y_coordinate),
                             )

        self.master.minsize(self.window_width, self.window_height)

    def __init__(self, master):
        self.master = master

        # Get the user_model
        self.db = user_model.UserDB()

        self.config_master()
        self.style = Style("litera")
        style_configurations(self)

        self.create_account_frame = ttk.Frame(self.master, padding="30")
        self.create_account_frame.pack(expand=False)

        self.title_label = ttk.Label(self.create_account_frame,
                                     text="CREATE ACCOUNT",
                                     style="title_label.TLabel",
                                     )
        self.title_label.grid(row=0,
                              column=0,
                              columnspan=2,
                              sticky="n",
                              pady=(5, 20)
                              )

        self.id_number_label = ttk.Label(
            self.create_account_frame, text="ID Number", style="form_label.TLabel")
        self.first_name_label = ttk.Label(
            self.create_account_frame, text="First Name", style="form_label.TLabel")
        self.last_name_label = ttk.Label(
            self.create_account_frame, text="Last Name", style="form_label.TLabel")
        self.password_label = ttk.Label(
            self.create_account_frame, text="Password", style="form_label.TLabel")
        self.confirm_password_label = ttk.Label(
            self.create_account_frame, text="Confirm Password", style="form_label.TLabel")

        self.id_number_entry = ttk.Entry(
            self.create_account_frame, font=(heading_font, h5), width=50)
        self.password_entry = ttk.Entry(self.create_account_frame, font=(
            heading_font, h5), width=50, show="*")
        self.confirm_password_entry = ttk.Entry(self.create_account_frame, font=(
            heading_font, h5), width=50, show="*")
        self.first_name_entry = ttk.Entry(
            self.create_account_frame, font=(heading_font, h5), width=23)
        self.last_name_entry = ttk.Entry(self.create_account_frame, font=(
            heading_font, h5), width=23)

        self.create_account_button = ttk.Button(self.create_account_frame,
                                                text="Create Account",
                                                style="success.TButton",
                                                command=self.validate)
        self.cancel_button = ttk.Button(self.create_account_frame,
                                        text="Cancel",
                                        style="secondary.Outline.TButton",
                                        command=self.cancel_button_clicked
                                        )

        self.first_name_label.grid(
            row=1, column=0, pady=10, padx=(130, 0), sticky="w")
        self.last_name_label.grid(
            row=1, column=1, pady=10, padx=(0, 130), sticky="w")
        self.first_name_entry.grid(
            row=2, column=0, pady=(0, 10), padx=(130, 30), sticky="w")
        self.last_name_entry.grid(
            row=2, column=1, pady=(0, 10), padx=(0, 130), sticky="w")
        self.id_number_label.grid(
            row=3, column=0, columnspan=2, pady=10, padx=130, sticky="w")
        self.id_number_entry.grid(
            row=4, column=0, columnspan=2, pady=(0, 10), padx=130, sticky="w")
        self.password_label.grid(
            row=5, column=0, columnspan=2, pady=10, padx=130, sticky="w")
        self.password_entry.grid(
            row=6, column=0, columnspan=2, pady=(0, 10), padx=130, sticky="w")
        self.confirm_password_label.grid(
            row=7, column=0, columnspan=2, pady=10, padx=130, sticky="w")
        self.confirm_password_entry.grid(
            row=8, column=0, columnspan=2, pady=(0, 10), padx=130, sticky="w")
        self.cancel_button.grid(
            row=9, column=0, pady=(35, 10), padx=(128, 0), sticky="w")
        self.create_account_button.grid(
            row=9, column=1, pady=(35, 10), padx=(0, 128), sticky="w")

    def validate(self):

        """
        id_number = 'C20101098'
        first_name = 'Luc Charl'
        last_name = 'Dato'
        password = '12345'
        confirm_password = '12345'
        """

        id_number = self.id_number_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if id_number == "" or first_name == "" or last_name == "" or password == "" or confirm_password == "":
            messagebox.showerror("Error", "Please fill in all the fields!")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
        else:
            new_user = user_model.User(id_number, first_name, last_name, password)
            print(repr(new_user))
            if self.db.create_user(new_user) == True:
                messagebox.showinfo("Success", "User is created successfully")
                self.create_account_frame.destroy()
                login_view.Login(self.master)
            else:
                messagebox.showerror("Error", "User is not created successfully")


    def cancel_button_clicked(self):
        self.create_account_frame.destroy()

        login_view.Login(self.master)


if __name__ == '__main__':
    root = ttk.Window()
    root.state("zoomed")
    root.resizable(0, 0)
    CreateAccount(root)
    root.mainloop()
