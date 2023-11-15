import sqlite3

class User:
    @staticmethod
    def read_users():
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute("SELECT id_number, password, first_name,last_name FROM users")
        
        rows = cursor.fetchall()
        user_dict = {}

        for row in rows:
            id_number, password, first_name, last_name = row
            user_dict[id_number] = {'password': password, 'first_name': first_name, 'last_name': last_name}

        cursor.close()
        return user_dict

