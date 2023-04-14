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


def print_exception(error):
    print('SQLite error: %s' % (' '.join(error.args)))
    print("Exception class is: ", error.__class__)
    print('SQLite traceback: ')
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))


class UserDB:

    def __init__(self):
        self.connect = sqlite3.connect('../database/kiosk.db')
        self.cursor = self.connect.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id_number TEXT PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.connect.commit()


    def create_user(self, user: User):
        """Create user account based from a user object.

        Args:
            user: User object

        Returns:
            bool: returns true if the creation and successful, false if not
        """
        try:
            self.cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
                             (user.id_number, user.password, user.first_name, user.last_name, ))
            self.connect.commit()
            return True
        except sqlite3.Error as er:
            print_exception(er)
            return False
        

    def get_user(self, id_number):
        try:
            self.cursor.execute('SELECT * FROM users WHERE id_number = ?', (id_number, ))
            row = self.cursor.fetchone()
            if row:
                return User(*row)
            else:
                return None
        except sqlite3.Error as er:
            print_exception(er)
            return False
        

    def update_user(self, user):
        try:
            self.cursor.execute("UPDATE users SET first_name = ?, last_name = ?, password = ? WHERE id_number = ?",
                                (user.first_name, user.last_name, user.password, user.id_number, ))
            self.connect.commit()
            return True
        except sqlite3.Error as er:
            print_exception(er)
            return False


    def delete_user(self, id_number):
        try:
            self.cursor.execute('DELETE FROM users WHERE id_number = ?', (id_number,))
            self.conn.commit()
            return True
        except sqlite3.Error as er:
            print_exception(er)
            return False
        

    def get_all_users(self):
        try:
            self.cursor.execute('SELECT * FROM users')
            rows = self.cursor.fetchall()
            return [User(*row) for row in rows]
        except sqlite3.Error as er:
            print_exception(er)
            return False
        

    def close(self):
        try:
            self.connect.close()
            return True
        except sqlite3.Error as er:
            print_exception(er)
            return False