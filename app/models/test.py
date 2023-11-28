import sqlite3


class Test:
    @staticmethod
    def new_last_test_id():
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tests ORDER BY TestID DESC LIMIT 1")

        last_row = cursor.fetchone()

        cursor.close()
        connection.close()

        if last_row == None:
            return "WattWise-T1"

        last_id = last_row[0]

        prefix, numeric_part = last_id.split("-T")
        incremented_numeric_part = str(int(numeric_part) + 1).zfill(len(numeric_part))
        return f"{prefix}-T{incremented_numeric_part}"

    @staticmethod
    def create_test(test_id, test_title, id_number, correct_answers, test_taken):
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO tests (TestID, TestTitle, UserIDNumber, CorrectAnswers, TestTaken) VALUES (?, ?, ?, ?, ?)",
                (test_id, test_title, id_number, correct_answers, test_taken),
            )
            connection.commit()
            print("Test created successfully!")
        except sqlite3.Error as e:
            print(f"Error creating test: {e}")
        finally:
            connection.close()
