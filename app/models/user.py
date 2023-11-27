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
            user_dict[id_number] = {
                "password": password,
                "first_name": first_name,
                "last_name": last_name,
            }

        cursor.close()
        connection.close()
        return user_dict

    @staticmethod
    def read_student_names():
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute("SELECT first_name || ' ' || last_name as Name FROM users")

        rows = cursor.fetchall()

        cursor.close()
        connection.close()
        return [row[0] for row in rows]

    @staticmethod
    def read_id_numbers():
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute("SELECT id_number as Name FROM users")

        rows = cursor.fetchall()

        cursor.close()
        connection.close()
        return [row[0] for row in rows]

    @staticmethod
    def register_user(first_name, last_name, id_number, password):
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (first_name, last_name, id_number, password) VALUES (?, ?, ?, ?)",
                (first_name, last_name, id_number, password),
            )
            connection.commit()
            print("User registered successfully!")
        except sqlite3.Error as e:
            print(f"Error registering user: {e}")
        finally:
            connection.close()
