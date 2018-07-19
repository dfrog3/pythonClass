def Math(userNumber):
    y= 0
    for i in range(userNumber+1):
        y += i**2
        
    print(y)
def main():
    print("give me a number")
    userNumber = int(input())
    Math(userNumber)
main()
