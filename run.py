import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# Import Views
import views.login_test_view as LoginView

if __name__ == '__main__':
    root = tk.Tk()
    LoginView.Login(root)
    root.mainloop()
