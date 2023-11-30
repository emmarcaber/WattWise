import sqlite3
import re


class Test:
    @staticmethod
    def new_last_test_id():
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tests")

        last_row = cursor.fetchall()[-1]

        cursor.close()
        connection.close()

        if last_row == None:
            return "WattWise-T1"

        last_test_id = last_row[0]

        # Create a nested function for incrementing the test_id
        def increment(test_id):
            def increase_version(match):
                version_number = int(match.group(1))
                new_version = version_number + 1
                return f"WattWise-T{new_version}"

            pattern = re.compile(r"WattWise-T(\d+)")
            return pattern.sub(increase_version, test_id)

        result = increment(last_test_id)

        return result

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
