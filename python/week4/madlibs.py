fromFileToLines = open("madLibsFiles/panda.txt", "r")
doneFile = open("madLibsFiles/done.txt", "w")
listOfLines = fromFileToLines.readlines()
print(listOfLines)
for lines in listOfLines:
    aSingleLine = lines.split()
    finLine =[]
    for words in aSingleLine:
        if "VERB" in words:
            print("Please enter a Verb ")
            putIn = input()
        elif "ADVERB" in words:
            print("Please enter an Adverb ")
            putIn = input()
        elif "NOUN" in words:
            print("Please enter a Noun ")
            putIn = input()
        elif "ADJECTIVE" in words:
            print("Please enter an Adjective ")
            putIn = input()
        elif "VERB." in words:
            print("Please enter a Verb ")
            putIn = input() + "."
        elif "ADVERB." in words:
            print("Please enter an Adverb ")
            putIn = input() + "."
        elif "NOUN." in words:
            print("Please enter a Noun ")
            putIn = input() + "."
        elif "ADJECTIVE." in words:
            print("Please enter an Adjective ")
            putIn = input() + "."
        else:
            putIn = words
        finLine.append(putIn)
    #print(finLine)
    finLine = " ".join(finLine)
    #print(finLine)
    doneFile.write(str(finLine) + "\n")
fromFileToLines.close()
doneFile.close()