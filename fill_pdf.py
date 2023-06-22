from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf(template_path, output_path, texts, coordinates):
    # Create a new PDF with Reportlab
    c = canvas.Canvas('temp.pdf', pagesize=letter)
    width, height = letter
    
    for text, coord in zip(texts, coordinates):
        c.drawString(coord[0], height - coord[1], text)
    
    c.save()

    # Read the template and overlay with the temporary PDF
    template = PdfReader(template_path)
    overlay = PdfReader('temp.pdf')

    # Merge the pages
    page = template.pages[0]
    page.merge_page(overlay.pages[0])

    # Write the output
    output = PdfWriter()
    output.add_page(page)
    with open(output_path, "wb") as output_pdf:
        output.write(output_pdf)

# Usage:
texts = ['Hello, World!', 'Hello, Again!']
coordinates = [(233, 36), (318, 72)]
create_pdf('template.pdf', 'output.pdf', texts, coordinates)
