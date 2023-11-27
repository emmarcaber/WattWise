import sqlite3


class Question:
    @staticmethod
    def get_questions_by_subcategories(subcategory_name):
        db_path = "app/database/kiosk.db"
        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute(
            """
                       SELECT QuestionID, QuestionText, CorrectOption 
                       FROM questions INNER JOIN subcategories ON subcategories.SubcategoryID = questions.SubcategoryID
                       WHERE SubcategoryName = ?
                       """,
            (subcategory_name,),
        )
        connection.commit()

        row = cursor.fetchall()

        questions = []
        for question in row:
            q = {"id": question[0], "text": question[1], "correct_option": question[2]}
            questions.append(q)

        cursor.close()
        connection.close()
        return questions
