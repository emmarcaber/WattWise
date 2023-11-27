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
        incremented_numeric_part = str(int(numeric_part) + 1)
        return f"{prefix}-T{incremented_numeric_part}"
