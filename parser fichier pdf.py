import PyPDF2

pdfFileObj = open('parsePDF.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObject = pdfReader.getPage(0)

print(pageObject.extractText())

pdfFileObj.close()