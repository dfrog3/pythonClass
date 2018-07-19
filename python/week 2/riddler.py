# compare 4 digits to make sure they are diffrent
# digits in thousends = digit in 10 *3
# number is odd
# check sum to be 27
# while loop to test numbers
# machine to make numbers



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

    print(str(digit1000)+ str(digit100)+ str(digit10)+ str(digit1))

main()







