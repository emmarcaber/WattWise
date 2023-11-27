import sqlite3


class Option:
    @staticmethod
    def get_options_by_subcategories(subcategory_name):
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute(
            """
                       SELECT OptionLetter, OptionText, questions.QuestionID FROM options
                       INNER JOIN questions ON options.QuestionID = questions.QuestionID
                       INNER JOIN subcategories ON subcategories.SubcategoryID = questions.SubcategoryID
                       WHERE SubcategoryName = ?
                       """,
            (subcategory_name,),
        )
        connection.commit()

        row = cursor.fetchall()

        options = []

        for option in row:
            o = {"option": option[0], "text": option[1], "questionId": option[2]}
            options.append(o)

        cursor.close()
        connection.close()
        return options
