import PyPDF2

pdfFile = open ("encryptedminutes.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFile)
print(pdfReader.isEncrypted)
pdfReader.decrypt("rosebud")
print(pdfReader.isEncrypted)

