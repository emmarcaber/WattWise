import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# Heading Font Sizes
h1_fs = 39
h2_fs = 31
h3_fs = 25
h4_fs = 20
h5_fs = 14
h6_fs = 13

heading_font = 'Arial'
normal_font = 'Century Gothic'


def style_configurations(self):

    self.style.configure("title_label.TLabel", font=(
        normal_font, h5_fs), width=50, padding=10, foreground='white', justify="center")

    self.style.configure("id_number_label.TLabel",
                         foreground='white', font=(normal_font, h5_fs), width=38)
    self.style.configure("primary.TButton", font=(
        normal_font, h5_fs), width=50, padding=10)
    self.style.configure("primary.Outline.TButton", font=(
        normal_font, h5_fs), width=50, padding=10)


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("WattWise")
        self.master.geometry("500x500")
        self.style = Style(theme='darkly')

        style_configurations(self)

        self.login_frame = ttk.Frame(self.master, padding="30")
        self.login_frame.pack(expand=True)

        self.title_label = ttk.Label(
            self.login_frame, text="WattWise : Kiosk Test Generator and Checker", style="title_label.TLabel")
        self.title_label.pack(pady=(0, 0))

        self.id_number_label = ttk.Label(self.login_frame, style="id_number_label.TLabel", text="ID Number:", )
        self.id_number_label.pack(pady=(0, 0))
        self.id_number_entry = ttk.Entry(self.login_frame, width=68)
        self.id_number_entry.pack(pady=(10, 10))

        self.password_label = ttk.Label(self.login_frame, style="id_number_label.TLabel", text="Password:", )
        self.password_label.pack(pady=(0, 0))
        self.password_entry = ttk.Entry(self.login_frame, show="*", width=68)
        self.password_entry.pack(pady=(10, 10))

        self.login_button = ttk.Button(self.login_frame, style="primary.TButton", text="Login", command=self.login,
                                       width=35)
        self.login_button.pack(padx=10, pady=10)

        self.register_button = ttk.Button(self.login_frame, style="primary.Outline.TButton", text="Create Account",
                                          command=self.create_account,
                                          )
        self.register_button.pack(padx=10, pady=10)

        self.message_label = ttk.Label(self.login_frame, text="")
        self.message_label.pack(pady=10)

    def login(self):
        pass

    def create_account(self):
        self.login_frame.destroy()

        account_window = self.master
        account_window.title("Create Account")
        account_window.geometry("500x500")

        style_configurations(self)

        account_frame = ttk.Frame(account_window, padding="30")
        account_frame.pack(expand=True)

        id_number_label = ttk.Label(account_frame, style="id_number_label.TLabel", text="ID Number:", )
        id_number_label.pack(pady=(0, 0))
        id_number_entry = ttk.Entry(account_frame, width=68)
        id_number_entry.pack(pady=(10, 10))

        password_label = ttk.Label(account_frame, style="id_number_label.TLabel", text="Password:", )
        password_label.pack(pady=(0, 0))
        password_entry = ttk.Entry(account_frame, show="*", width=68)
        password_entry.pack(pady=(10, 10))

        confirm_password_label = ttk.Label(account_frame, style="id_number_label.TLabel", text="Confirm Password:")
        confirm_password_label.pack(pady=(0, 5))
        confirm_password_entry = ttk.Entry(account_frame, show="*", width=68)
        confirm_password_entry.pack(pady=(0, 10))

        message_label = ttk.Label(account_frame, text="")
        message_label.pack(pady=10)

        submit_button = ttk.Button(account_frame, style="primary.TButton", text="Create",
                                   command=self.submit_account)
        submit_button.pack(pady=10)

    def submit_account(self):
        pass

    def insert_db(self, id_number, password):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
