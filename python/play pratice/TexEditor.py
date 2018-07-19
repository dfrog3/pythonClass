import os



theFile = open("tex/myFirstTex.tex", "r")
output = open("out/fin.tex", "w")
texlines=theFile.readlines()
#print(texlines)
for line in texlines:
    if "\\begin{center}" in line:
        print(line)
        output.write(line)
        output.write("\n        hello")
    else:
        output.write(line)

theFile.close()
output.close()
os.system("pdflatex out/fin.tex")
os.system("mv fin.pdf ./out/fin.pdf")
os.system("rm fin.aux")
os.system("rm fin.log")

