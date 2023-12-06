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
    def is_test_checked(test_id):
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute(
            "SELECT Status FROM tests WHERE TestID = ?",
            (test_id,),
        )

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        return True if row[0] != "PENDING" else False

    @staticmethod
    def test_belong_to_current_user(test_id, student_id):
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM tests WHERE TestID = ? AND UserIDNumber = ?",
            (
                test_id,
                student_id,
            ),
        )

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        if row is None:
            return False

        return True

    @staticmethod
    def get_correct_answers_of_test_from_db(test_id):
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute(
            "SELECT CorrectAnswers FROM tests WHERE TestID = ?",
            (test_id,),
        )

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        return row[0]

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

    @staticmethod
    def update_score_of_tests_in_db(score, test_id):
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        try:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE tests SET Score = ?, Status = 'CHECKED' WHERE TestID = ?",
                (score, test_id),
            )
            connection.commit()
            print("Test updated successfully!")
        except sqlite3.Error as e:
            print(f"Error updating test: {e}")
        finally:
            connection.close()

    @staticmethod
    def get_total_tests_of_user(student_id):
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute(
            """
                SELECT COUNT(*) FROM tests
                JOIN users ON tests.UserIDNumber = users.id_number
                WHERE users.id_number = ?
            """,
            (student_id,),
        )

        row = cursor.fetchone()

        result = row[0]

        cursor.close()
        connection.close()

        return result

    @staticmethod
    def get_total_tests_per_subcategory_of_user(student_id):
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute(
            """
                SELECT TestTitle FROM tests
                JOIN users ON tests.UserIDNumber = users.id_number
                WHERE users.id_number = ?
            """,
            (student_id,),
        )

        rows = cursor.fetchall()

        esas_taken = 0
        math_taken = 0
        eeps_taken = 0

        for row in rows:
            if "ESAS" in row[0]:
                esas_taken += 1
            elif "Mathematics" in row[0]:
                math_taken += 1
            elif "EEPS" in row[0]:
                eeps_taken += 1

        cursor.close()
        connection.close()

        return [esas_taken, math_taken, eeps_taken]

    @staticmethod
    def get_tests_from_db(student_id):
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute(
            """
                SELECT TestID, TestTitle, TestTaken, Score, Status FROM tests
                JOIN users ON tests.UserIDNumber = users.id_number
                WHERE users.id_number = ?
            """,
            (student_id,),
        )

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        return rows
