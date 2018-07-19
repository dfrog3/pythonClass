import PyPDF2
rawfile = open("encrypted.pdf","rb")
dict = open("dictionary.txt", "r")
pdffile = PyPDF2.PdfFileReader(rawfile)




def decrypt():
    for words in dict.readlines():
        word = words[0:len(words)-1].lower()

        if pdffile.decrypt(word) == 1:
            return word

print(decrypt())

