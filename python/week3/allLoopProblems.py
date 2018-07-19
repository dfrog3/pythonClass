def vowel(userString):



    x = 0

    vowels = "aeiou"

    for letter in userString.lower():
        if letter in vowels:
            x = x + 1
        else:
            continue
    return x



def ArmChecker(x):


    if len(x) != 3:  # checks digits
        return "This is not a three digit number"
    else:

        counter = int(x)
        for i in range(0, 3):  # sorts digits
            j = counter % 10
            counter = counter // 10
            if i == 0:
                number3 = j
            elif i == 1:
                number2 = j
            elif i == 2:
                number1 = j
        # print(number1, number2, number3)

        # does math
        if (number1 * number1 * number1 + number2 * number2 * number2 + number3 * number3 * number3) == int(x):
            return "This is an Armstrong number"
        else:
            return "This is not an Armstrong number"

def digits(ourInt):


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

def DifrentChecker(digit1, digit10, digit100, digit1000): #checks if digits are the same
    digits = str(digit1) + str(digit10) + str(digit100) + str(digit1000)
    digits = int(digits) #merges digits
    for i in range(0, 4):
        x = digits % 10
        digits = digits // 10 # cuts up string of digits
        y = str(digits)
        if str(x) in y: #checks for same char
            return False
    return True

def riddle():
    digit1 = -1
    digit10 = 0
    digit100 = 0
    digit1000 = 0

    diffrent = False
    SUM = False

    while not(SUM == True and diffrent == True):
       # adds 2 to final digit
        digit1 += 2
        if digit1 > 9:
            digit1 = 1
        #checks conditions
        if digit1 + digit10 + digit100 + digit1000 == 27:
            SUM = True #checks sum
        else: SUM = False
        diffrent = DifrentChecker(digit1, digit10, digit100, digit1000) # checks if they are the same
        if SUM == True & diffrent == True: #checks to continue
            break
        # adds 1 to digit 10 and also handles digit 1000
        digit10 += 1
        if digit10 > 3:
            digit10 = 0
        digit1000 = digit10 * 3

           # checks conditions
        if digit1 + digit10 + digit100 + digit1000 == 27:
            SUM = True  # checks sum
        else:
            SUM = False
        diffrent = DifrentChecker(digit1, digit10, digit100, digit1000)  # checks if they are the same
        if SUM == True & diffrent == True:  # checks to continue
            break



        digit100 += 1
        if digit100 > 9:
            digit100 = 1

            # checks conditions
        if digit1 + digit10 + digit100 + digit1000 == 27:
            SUM = True  # checks sum
        else:
            SUM = False
        diffrent = DifrentChecker(digit1, digit10, digit100, digit1000)  # checks if they are the same
        if SUM == True & diffrent == True:  # checks to continue
            break

    return (str(digit1000)+ str(digit100)+ str(digit10)+ str(digit1))

print("give me a string")
userString = input()
x = vowel(userString)
print(x)

print("Enter a 3 digit number")
x = input()
print(ArmChecker(x))

print("give me an int")
ourInt = input()
print(digits(ourInt))


print(riddle())