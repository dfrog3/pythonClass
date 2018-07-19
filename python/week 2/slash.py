def rowFinder(base):
    length = 2
    for p in range(base-1):
        length = length + 4
    return length

def main():

    print("Give me an int")
    base = int(input())





    rowLength = rowFinder(base)
    x = rowLength

    for i in range(base+1):
        point = ""
        for j in range(x):
            point = point + "!"
        x -= 4

        slash1 = ""
        slash2 = ""

        if i != base:
            for j in range(i):
                slash1 = slash1 + "\\\\"
                slash2 = slash2 + "//"
        else:
            break

        print(slash1 + point + slash2)




main()