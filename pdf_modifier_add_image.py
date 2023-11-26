import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import io

def add_qrcode_to_pdf(input_pdf_path, output_pdf_path, image_path):
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(open(input_pdf_path, 'rb'))

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
        can.drawImage(image_path, x, y, width=1.43 * inch, height=1.43 * inch)

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
    with open(output_pdf_path, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf_path = "answer_sheet.pdf"  # Replace with the path to your input PDF file
    output_pdf_path = "output.pdf"  # Replace with the desired output PDF file path
    image_path = "example_qrcode.png"  # Replace with the path to your image file

    add_qrcode_to_pdf(input_pdf_path, output_pdf_path, image_path)
