from pdf2docx import Converter

pdf_path = "sayısal hesaplama.pdf"
docx_path = "sayısal hesaplama.docx"

cv = Converter(pdf_file=pdf_path)
cv.convert(docx_filename=docx_path)
cv.close()
