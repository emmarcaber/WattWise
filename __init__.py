import sys
sys.path.append('../')

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style

# import create_account_view
from config.styles import (h1, h2,
                           h3, h4,
                           h5, h6,
                           normal_font, heading_font)

# Import Views
import views.login_test_view as login_view

if __name__ == '__main__':
    root = ttk.Window()
    login_view.Login(root)
    root.mainloop()
