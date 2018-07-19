def LineMaker(tableSize):
    y = 0
    m = 0
    for x in range(1, tableSize+1):

        y = 0
        output = ""

        for i in range(tableSize):

            y += x
            output = output + " "+ str(y)
        print(output)


def main():
    print("give me a starting number")
    tableSize = int(input())
    LineMaker(tableSize)
main()