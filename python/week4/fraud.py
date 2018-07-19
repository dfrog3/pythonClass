

def countDigits(ourInt):
    ourInt = str(ourInt)
    ourIntLen = len(ourInt)
    answer = 0
    if int(ourInt) < 0:
        ourInt = int(ourInt) * -1
        ourIntLen -= 1
    ourInt = int(ourInt)
    for i in range(0, ourIntLen, 1):
        base = ourInt % 10
        #print(base)
        ourInt = ourInt // 10
        x = base
        if base != 0:
            for j in range(1, x):
                base -= 1
        else:
            base += 1
        answer = answer + base
    return answer

def nthDigitBack(n, num):#done
    for i in range(0, n):
        num = num // 10
    return num % 10




def nthDigit(n, num):#done
    try:
        return int(str(num)[n])
    except:
        return 0


def updateTally(n, num, tally):
    fromN = nthDigit(n,num)
    if fromN == 0:
        tally[0] = tally[0] +1

    elif fromN == 1:
        tally[1] = tally[1] + 1

    elif fromN == 2:
        tally[2] = tally[2] + 1

    elif fromN == 3:
        tally[3] = tally[3] + 1

    elif fromN == 4:
        tally[4] = tally[4] + 1

    elif fromN == 5:
        tally[5] = tally[6] + 1

    elif fromN == 6:
        tally[6] = tally[6] + 1

    elif fromN == 7:
        tally[7] = tally[7] + 1

    elif fromN == 8:
        tally[8] = tally[8] + 1

    elif fromN == 9:
        tally[9] = tally[9] + 1



def nthDigitTally(n,nums, tally):
    for num in nums:
        updateTally(n,num,tally)


def readMysteriousNumbers(y):
    theFile = open(y,"r")
    theRaw = theFile.read()
    theRefined = theRaw.split()
    #print(theRefined)
    return theRefined

def main(n, x):
    tally = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    nums = readMysteriousNumbers(x)

    nthDigitTally(n,nums, tally)
    return tally

print(main(0, "librarybooks.txt"))

