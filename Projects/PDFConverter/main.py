from pdf2docx import Converter

pdf_file = input('pdf url: ')
docx_file = 'output.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close