def ArmChecker():
    print("Enter a 3 digit number")
    x = input()

    if len(x) != 3: #checks digits
        return "This is not a three digit number"
    else:

        counter = int(x)
        for i in range(0,3): #sorts digits
            j = counter % 10
            counter = counter // 10
            if i == 0:
                number3 = j
            elif i == 1:
                number2 = j
            elif i == 2:
                number1 = j
        #print(number1, number2, number3)


        #does math
        if (number1 * number1 * number1 + number2 * number2 * number2 + number3 * number3 * number3) == int(x) :
            print("This is an Armstrong number")
        else:
            return print("This is not an Armstrong number")




