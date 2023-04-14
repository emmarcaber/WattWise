"""User Model

Description:
    Model for manipulating the User table inside the Database
"""
import sqlite3
import sys
import traceback


class User:
    def __init__(self, id_number: str, first_name: str, last_name: str, password: str):
        """Create a user instance.

        Args:
            id_number (string): User ID Number
            first_name (string): User First Name
            last_name (string): User Last Name
            password (string): User Password
        """
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def __repr__(self):
        return f"User('{self.id_number}', '{self.first_name}', '{self.last_name}')"


class UserDB:
    def __init__(self):
        self.conn = sqlite3.connect('../database/kiosk.db')
        self.cur = self.conn.cursor()

        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id_number TEXT PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def create_user(self, user: User):
        """Create user account based from a user object.

        Args:
            user: User object

        Returns:
            bool: returns true if the creation and successful, false if not
        """
        try:
            self.cur.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
                             (user.id_number, user.first_name, user.last_name, user.password))
            self.conn.commit()
            return True
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
            return False
