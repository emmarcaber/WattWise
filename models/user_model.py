import sqlite3
from tkinter import messagebox


class User:
    def __init__(self, id_number, password, first_name, last_name):
        self.conn = sqlite3.connect("../database/kiosk.db")
        self.cur = self.conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id_number INTEGER, "
                         "password VARCHAR, firstname TEXT, lastname TEXT)")
        self.conn.commit()

        self.insert(id_number, password, first_name, last_name)

    def insert(self, id_number, password, first_name, last_name):

        try:
            self.cur.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (id_number, password, first_name, last_name))
            self.conn.commit()
            messagebox.showinfo("Success", "Data inserted successfully!")
        except:
            messagebox.showerror("Error", "Failed to insert data!")

    def __del__(self):
        self.conn.close()
