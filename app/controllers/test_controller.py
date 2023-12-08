import qrcode
import PyPDF2
import io
import os
import aspose.pdf as pdf

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
        output_folder = "../print_check"

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

        self.excess_questionnaire_page_path = os.path.normpath(
            os.path.join(
                current_directory, output_folder, "excess_questionnaire_page.pdf"
            )
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
        self, student_name, id_number, category_subcategory, test_id
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
            can.drawString(x + 3, y, test_id)

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
        question_style.fontSize = 10
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
        self.modify_answer_sheet(
            student_name, student_id, category_subcategory, test_id
        )
        self.create_questionnaire(questions, test_id)
        self.merge_answer_sheet_and_questionnaire()

    def is_questionnaire_five_pages(self):
        with open(self.questionnaire_path, "rb") as file:
            # Create PDF Reader and Writer
            pdf_reader = PyPDF2.PdfReader(file)
            pdf_writer = PyPDF2.PdfWriter()

            # Get all the total pages of the questionnaire
            total_pages = len(pdf_reader.pages)

            # If questionnaire has five pages, get the last page
            # then create a new PDF file from that page and return True
            if total_pages == 5:
                last_page = pdf_reader.pages[-1]
                pdf_writer.add_page(last_page)

                # Create the pdf file from the last page
                with open(self.excess_questionnaire_page_path, "wb") as output_file:
                    pdf_writer.write(output_file)
                    return True

            # Else, just return false
            return False

    def print_questionnaire_answer_sheet(self):
        qa_files = [self.questionnaire_path, self.answer_sheet_with_qr_path]

        # If the questionnaire has five pages, insert the
        # excess_questionnaire_page_path in the middle
        if self.is_questionnaire_five_pages():
            qa_files.insert(1, self.excess_questionnaire_page_path)

        if not qa_files:
            print("No pdf files found in the specified directory.")
            return

        for file in qa_files:
            # Initialize PdfViewer class object
            viewer = pdf.facades.PdfViewer()

            # Bind PDF document
            viewer.bind_pdf(file)

            # Print the documents
            viewer.print_document()
