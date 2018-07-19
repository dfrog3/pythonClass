def add(num1, num2):
    """Returns num1 plus num2"""
    return num1 + num2

def sub(num1,num2):
    """Returns num1 minus num2"""
    return num1 - num2

def mul(num1, num2):
    """Returns num1 times num2"""
    return num1 * num2

def div(num1, num2):
    """Returns num1 divided by num2"""
    return num1 / num2

def main():
    """Allows you to run basic calculations with two numbers"""
    validInput = False
    num1 =""
    num2=""
    operation=""
    while type(num1) != int:
        try:
            num1 = int(input("What is number 1?"))
        except:
            print("not an int")
    while type(num2) != int:
        try:
            num2 = int(input("What is number 2?"))
        except:
            print("not ant int")
            
    while type(operation) != int:
        try:
            operation = int(input("What do you want to do? 1. add, 2. subtract, 3. multiply, or 4. divide"))
        except:
            print("not an int")

    # Determine operation
    if (operation == 1):
        print("Adding...")
        print(add(num1, num2))
    elif (operation == 2):
        print("Subtracting...")
        print(sub(num1, num2))
    elif (operation == 3):
        print("Multiplying...")
        print(mul(num1, num2))
    elif (operation == 4):
        print("Dividing...")
        print(div(num1, num2))
    else:
        print("I don't understand")

main()
