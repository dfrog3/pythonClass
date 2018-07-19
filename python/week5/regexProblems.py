import re
import random
diction = open("words.txt","r")
wordUnsplit = diction.read()
wordSplit = wordUnsplit.split()

def animals(wordSplit):
    regex = re.compile(r"^.*cat|dog|Cat|Dog.*$")
    out = []
    for word in wordSplit:
        canidate = regex.findall(word)
        if canidate != []:
            out.append(canidate)
            continue
    return out


def fourLetter(wordSplit):
    regex = re.compile(r"^[a-z]{4}$",re.IGNORECASE)
    out =[]
    for word in wordSplit:
        x = (regex.findall(word))
        if x != []:
            out.append(x)
    return out


def ingIon(wordSplit):
    ion = re.compile(r"^.*ion$")
    ing = re.compile(r"^.*ing$")
    ionC = []
    ingC= []
    for word in wordSplit:
        canidate = ion.findall(word)
        if canidate != []:
            ionC.append(canidate)
            continue

        canidate = ing.findall(word)
        if canidate != []:
            ingC.append(canidate)
            continue

    if len(ingC)>len(ionC):
        return ("Ing", len(ingC))
    else:
        return ("ion", len(ionC))


def qnotU(wordSplit):
    regex = re.compile(r"^.*[qQ][^Uu]*$")
    out =[]
    for word in wordSplit:
        canidate = regex.findall(word)
        if canidate != []:
            out.append(canidate)
            continue

    return out


def noV(wordSplit):
    regex = re.compile(r"^[^AEIOUaeiou]*$")
    out = []
    for word in wordSplit:
        canidate = regex.findall(word)
        if canidate != []:
            out.append(canidate)
    return out

def twoV (wordSplit):
    regex = re.compile(r"^\w*[aeiouAEIOU]{2}.*$")
    out = []
    for word in wordSplit:
        canidate = regex.findall(word)
        if canidate != []:
            out.append(canidate)
    return out


def atwo (wordSplit):
    regex = re.compile(r"^[^aeiouAEIOU]*[aeiouAEIOU][aeiouAEIOU][^aeiouAEIOU]*$")
    out = []
    for word in wordSplit:
        canidate = regex.findall(word)
        if canidate != []:
            out.append(canidate)
    return out

def nakamoto(name):
    regex = re.compile(r"^[A-Z][a-z A-Z^\d]* Nakamoto$")
    check = regex.findall(name)
    if check == []:
        return False
    else:
        return True


def sCheck(word):
    regex = re.compile(r"^(twenty|thirty|fourty|fifty|sixty|seventy|eighty|ninety)-(one|two|three|four|five|six|seven|eight|nine)$")
    temp = regex.fullmatch(word)
    try:
        check = temp[0]
    except:
        return False
    if check == word:
        return True
    else:
        return False

def password(word):
    cLen = re.compile(r"^.{8}$")
    cUp = re.compile(r"^.*[A-Z].*$")
    cLow = re.compile(r"^.*[a-z].*$")
    cDig = re.compile(r"^.*\d.*$")
    try:
        out = cDig.fullmatch(cUp.findall(cLow.findall(cLen.findall(word)[0])[0])[0])[0]
    except:
        return False
    if out == word:
        return True


def comic(wordSplit):
    x = fourLetter(wordSplit)
    theWords=[]
    for i in x:
        theWords.append(i[0])
    out=(str(random.choice(theWords))+str(random.choice(theWords))+str(random.choice(theWords))+str(random.choice(theWords)))
        


    return out




















print("animals",len(animals(wordSplit)))
print("4 letter words",len(fourLetter(wordSplit)))
print(ingIon(wordSplit))
print("no U's",len(qnotU(wordSplit)))
print("no vowels",len(noV(wordSplit)))
print("two touch vowels",len(twoV(wordSplit)))
print("two vowels",len(atwo(wordSplit)))
print("nakamoto",nakamoto("Mr. Nakamoto"))
print("number word", sCheck("thirty-one"))
print("password",password("1Abohcdu"))
print("comic", comic(wordSplit))
diction.close()



