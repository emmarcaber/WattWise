import qrcode
import PyPDF2
import io
import os

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class TestController:
    def create_paths(self):
        # Get the current working directory
        current_directory = (
            "C:/Users/caber/OneDrive/Documents/Coding/WattWise/app/controllers"
        )
        output_folder = "../print"

        # Construct the relative path
        self.qr_path = os.path.normpath(
            os.path.join(current_directory, output_folder, "qrcode.png")
        )

        self.answer_sheet_path = os.path.normpath(
            os.path.join(current_directory, output_folder, "answer_sheet.pdf")
        )

        self.test_paper_header_path = os.path.normpath(
            os.path.join(current_directory, output_folder, "test_paper_header.png")
        )

        self.answer_sheet_with_qr_path = os.path.normpath(
            os.path.join(current_directory, output_folder, "answer_sheet_with_qr.pdf")
        )

        self.questionnaire_path = os.path.normpath(
            os.path.join(current_directory, output_folder, "questionnaire.pdf")
        )

        self.final_paper_path = os.path.normpath(
            os.path.join(current_directory, output_folder, "Print.pdf")
        )

        # Create the output folder if it doesn't exist
        os.makedirs(os.path.join(current_directory, output_folder), exist_ok=True)

    def generate_qr_code(self, data):
        # Create QR Code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add data to the qr code
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        img.save(self.qr_path)

    def modify_answer_sheet(
        self,
        student_name,
        id_number,
        category_subcategory,
    ):
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(open(self.answer_sheet_path, "rb"))

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Loop through all the pages of the input PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get the page
            page = pdf_reader.pages[page_num]

            # Create a PDF canvas with A4 page size
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=A4)

            # Calculate the position for the upper right corner
            x = A4[0] - 2.35 * inch
            y = A4[1] - 2.55 * inch

            # Draw the image on the canvas
            can.drawImage(self.qr_path, x, y, width=1.43 * inch, height=1.43 * inch)

            # Draw the string on the canvas
            can.drawString(155, y + 30, student_name)
            can.drawString(155, y + 14, id_number)

            can.setFont("Helvetica", 10)
            can.drawString(155, y, category_subcategory)

            # Save the canvas to the buffer
            can.save()

            # Move the buffer position to the beginning
            packet.seek(0)

            # Create a PDF object from the canvas
            new_pdf = PyPDF2.PdfReader(packet)

            # Merge the two PDFs, overlaying the image on the original page
            page.merge_page(new_pdf.pages[0])

            # Add the modified page to the writer
            pdf_writer.add_page(page)

        # Write the result to the output PDF file
        with open(self.answer_sheet_with_qr_path, "wb") as output_file:
            pdf_writer.write(output_file)

    def create_questionnaire(self, questions, title):
        # Create a new PDF document with portrait orientation
        doc = SimpleDocTemplate(self.questionnaire_path, pagesize=A4, title=f"{title}")

        # Create a list to hold the flowable elements
        elements = []

        # Define the paragraph style for questions
        styles = getSampleStyleSheet()
        question_style = styles["Normal"]

        # Set the font size for questions
        question_style.fontName = "Helvetica"
        question_style.fontSize = 12
        question_style.leading = 15

        # Set the margin
        left_margin = 0.5 * inch
        right_margin = A4[0] - 0.5 * inch
        bottom_margin = 0.5 * inch
        top_margin = A4[1] - 0.5 * inch

        # Set the line spacing
        line_spacing = 0.3 * inch

        # Set the margin between question and options
        margin_between_question_and_options = 0.2 * inch

        # Create a paragraph style for options with padding
        option_style = ParagraphStyle(name="OptionStyle", parent=question_style)
        option_style.leftIndent = 0  # Remove any left indent
        option_style.paddingLeft = 0.1 * inch
        option_style.paddingRight = 0.1 * inch
        option_style.paddingTop = 0.05 * inch
        option_style.paddingBottom = 0.05 * inch
        option_style.leading = 15

        image = Image(self.test_paper_header_path, width=6 * inch, height=1 * inch)
        elements.append(image)

        title_style = ParagraphStyle(
            name="TitleStyle", parent=getSampleStyleSheet()["Title"]
        )
        title_text = f"ID: {title}"
        title_paragraph = Paragraph(title_text, title_style)
        elements.append(title_paragraph)

        elements.append(Spacer(1, margin_between_question_and_options))

        # Loop through the questions
        count = 1
        for question, details in questions.items():
            # Create a Paragraph for the question text
            question_text = f"{count}. {question}"
            question_paragraph = Paragraph(question_text, question_style)
            elements.append(question_paragraph)

            # Add a spacer to separate the question and options
            elements.append(Spacer(1, margin_between_question_and_options))

            # Create Paragraphs for the answer choices with the option_style
            options = details["options"]
            for option, text in options.items():
                option_text = f"{option}. {text}"
                option_paragraph = Paragraph(option_text, style=option_style)
                elements.append(option_paragraph)

            # Add a spacer to separate questions
            elements.append(Spacer(1, line_spacing))
            count += 1

        # Build the PDF document from the elements
        doc.build(elements)

    def merge_answer_sheet_and_questionnaire(self):
        merger = PyPDF2.PdfMerger()

        pdfs = [self.questionnaire_path, self.answer_sheet_with_qr_path]

        for pdf in pdfs:
            merger.append(pdf)

        merger.write(self.final_paper_path)
        merger.close()

    def generator(
        self, student_id, student_name, category_subcategory, test_id, questions
    ):
        self.create_paths()
        self.generate_qr_code(test_id)
        self.modify_answer_sheet(student_name, student_id, category_subcategory)
        self.create_questionnaire(questions, test_id)
        self.merge_answer_sheet_and_questionnaire()


# if __name__ == "__main__":
#     student_id = "1234567890"
#     student_name = "Angel Bianca Nacario"
#     category_subcategory = "Mathematics - Probability and Statistics"
#     test_id = "WattWise-T2"
#     questions = {
#         "What is the pH of a solution with a hydrogen ion concentration of 1 x 10^-9 M?": {
#             "options": {"A": "7", "B": "9", "C": "5", "D": "3", "E": "11"},
#             "correct_option": "B",
#         },
#         "What is the pH of a neutral solution?": {
#             "options": {"A": "9", "B": "8", "C": "7", "D": "6", "E": "5"},
#             "correct_option": "C",
#         },
#         "What is Avogadro's number?": {
#             "options": {
#                 "A": "6.02 x 10^23",
#                 "B": "14",
#                 "C": "0",
#                 "D": "7",
#                 "E": "22.4",
#             },
#             "correct_option": "A",
#         },
#         "What is the chemical name for table salt?": {
#             "options": {
#                 "A": "Ferrous Sulfate",
#                 "B": "Sodium Chloride",
#                 "C": "Dihydrogen Oxide",
#                 "D": "Sodium Dichloride",
#                 "E": "Iron Oxide",
#             },
#             "correct_option": "B",
#         },
#         "Which gas is commonly known as laughing gas?": {
#             "options": {
#                 "A": "Oxygen",
#                 "B": "Carbon dioxide",
#                 "C": "Nitrous oxide",
#                 "D": "Hydrogen",
#                 "E": "Helium",
#             },
#             "correct_option": "C",
#         },
#         "Which of the following is a transition metal?": {
#             "options": {
#                 "A": "Aluminum",
#                 "B": "Sodium",
#                 "C": "Calcium",
#                 "D": "Potassium",
#                 "E": "Iron",
#             },
#             "correct_option": "E",
#         },
#         "What is the chemical symbol for oxygen?": {
#             "options": {"A": "O", "B": "Ox", "C": "Oz", "D": "On", "E": "Oy"},
#             "correct_option": "A",
#         },
#         "Which element is a noble gas and commonly used in lighting?": {
#             "options": {
#                 "A": "Helium",
#                 "B": "Neon",
#                 "C": "Krypton",
#                 "D": "Argon",
#                 "E": "Radon",
#             },
#             "correct_option": "D",
#         },
#         "Which gas is responsible for the smell of rotten eggs?": {
#             "options": {
#                 "A": "Oxygen",
#                 "B": "Nitrogen",
#                 "C": "Hydrogen",
#                 "D": "Sulfur dioxide",
#                 "E": "Carbon dioxide",
#             },
#             "correct_option": "D",
#         },
#         "What is the name of the process where a substance changes directly from a gas to a solid without passing through the liquid phase?": {
#             "options": {
#                 "A": "Sublimation",
#                 "B": "Deposition",
#                 "C": "Condensation",
#                 "D": "Evaporation",
#                 "E": "Freezing",
#             },
#             "correct_option": "B",
#         },
#         "Which type of bond involves the sharing of electrons between atoms?": {
#             "options": {
#                 "A": "Ionic",
#                 "B": "Covalent",
#                 "C": "Metallic",
#                 "D": "Polar",
#                 "E": "Nonpolar",
#             },
#             "correct_option": "B",
#         },
#         "What is the chemical formula for water?": {
#             "options": {"A": "H2O2", "B": "CO2", "C": "H2SO4", "D": "NH3", "E": "H2O"},
#             "correct_option": "E",
#         },
#         "Which of the following is a halogen?": {
#             "options": {
#                 "A": "Calcium",
#                 "B": "Sodium",
#                 "C": "Fluorine",
#                 "D": "Potassium",
#                 "E": "Iron",
#             },
#             "correct_option": "C",
#         },
#     }

#     test = TestController()
#     test.generator(student_id, student_name, category_subcategory, test_id, questions)
