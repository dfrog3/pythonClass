def generateTriangleNumbers(fromusr):
    box=[]
    for i in range(1,fromusr+1):
        x = (i*(i+1))/2
        x = int(x)
        box.append(x)
    return box

print("give an int")
fromusr = int(input())
print(generateTriangleNumbers(fromusr))

def reverseone(toback):
    back = ""
    for i in range(len(toback),0,-1):
        back = back + toback[i-1]
    return back
def reverseAll(x):
    done = list(map(reverseone,x))
    return done

x = ["hello", "cello", "i'm", "mello"]
print(x)
print(reverseAll(x))

def reverseone(toback):
    back = ""
    for i in range(len(toback),0,-1):
        back = back + toback[i-1]
    return back



def isPalindrome(x):

    x = str(x)
    length = len(x)
    if length % 2 == 0:
        front = x[0:int((length / 2))]
        backRaw = x[int((length / 2)):length + 1]
    else:
        front = x[0:int(((length - 1) / 2))]
        backRaw = x[(int((length - 1) / 2)) + 1:length + 1]
    jar = reverseone(backRaw)

    if front.lower() == jar.lower():
        return True
    else:
        return False

print(isPalindrome("hiiH"))


def gap(x):
    output=[]
    for i in range(len(x)-1):
        #print(x[i])
        if x[i] > x[i+1]:
            c = (x[i])-(x[i+1])
        else:
            c = (x[i + 1]) - (x[i])
        #print(x[i],x[i+1],c)
        output.append(c)
    return output


def bubbleSort(thisList):
    for number in range(len(thisList) - 1, 0, -1):
        for i in range(number):
            if thisList[i]>thisList[i + 1]:
                jar = thisList[i]
                thisList[i] = thisList[i + 1]
                thisList[i + 1] = jar

x=[1,5,6,4,8,2,14,9,6,3,4,6,5,123,654,644,23,6,7]

step1 = list(gap(x))
#print(step1)
bubbleSort(step1)
print(step1[0])

theList = [1,2,3,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2]
def roundAllUp(theList):
    box = list(map(round, theList))
    return box
box = roundAllUp(theList)
print(box)


def bubbleSort(thisList):
    for number in range(len(thisList) - 1, 0, -1):
        for i in range(number):
            if thisList[i]>thisList[i + 1]:
                jar = thisList[i]
                thisList[i] = thisList[i + 1]
                thisList[i + 1] = jar
    return thisList

def isSorted(toCheck):
    check = list (toCheck)

    if check == bubbleSort(toCheck):
        return True
    else:
        return False

alist = [1,2]

print(isSorted(alist))