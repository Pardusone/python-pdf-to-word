from random import sample

from pdf2docx import Converter

pdf_file = "sample.pdf"
docx_file = "output.docx"

cv = Converter(pdf_file)  # Pass the PDF file directly
cv.convert(docx_file)     # Pass the DOCX file directly
cv.close()                # Always close the converter after conversion
