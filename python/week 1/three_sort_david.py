print("Hello, I will sort three integers for you.\nPlease enter the first integer now")
firstNumber = int(input())
print("Thank you.\nPlease enter the second integer.")
secondNumber = int(input())
print("Thank you.\n please eneter the last integer.")
thirdNumber = int(input())
#fills starting variables
if firstNumber < secondNumber and firstNumber < thirdNumber:
    smallestNumber = firstNumber
elif firstNumber < secondNumber and firstNumber > thirdNumber:
    middleNumber = firstNumber
elif firstNumber > secondNumber and firstNumber < thirdNumber:
    middleNumber = firstNumber    
elif firstNumber > secondNumber and firstNumber > thirdNumber: 
    largestNumber = firstNumber
else:
    print("error in first sort block")
#first number sorting code block
if secondNumber < firstNumber and secondNumber < thirdNumber:
    smallestNumber = secondNumber
elif secondNumber < firstNumber and secondNumber > thirdNumber:
    middleNumber = secondNumber
elif secondNumber > firstNumber and secondNumber < thirdNumber:
    middleNumber = secondNumber    
elif secondNumber > firstNumber and secondNumber > thirdNumber: 
    largestNumber = secondNumber
else:
    print("error in second sort block")
#second number sorting code block
if thirdNumber < secondNumber and thirdNumber < firstNumber:
    smallestNumber = thirdNumber
elif thirdNumber < secondNumber and thirdNumber > firstNumber:
    middleNumber = thirdNumber
elif thirdNumber > secondNumber and thirdNumber < firstNumber:
    middleNumber = thirdNumber    
elif thirdNumber > secondNumber and thirdNumber > firstNumber: 
    largestNumber = thirdNumber
else:
    print("error in third sort block")
#third number sorting code block
print("The results are in.\n", smallestNumber , middleNumber , largestNumber)
