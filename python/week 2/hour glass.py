def main():

    colon = 0
    space = 0



    for i in range(6, -7, -1):
        if i == 6:
            print("|", end='')
            for x in range(10):
                print("\"", end='')
            print("|")
            continue
        elif i == -6:
            print("|", end='')
            for x in range(10):
                print("\"", end='')
            print("|")
            continue
        elif i == 0:
            print("     ||")
            continue
        if i == 1:
            continue
        if i == -1:
            continue


        if i > 0:
            for j in range(i+1):
                if j == 0:
                    for k in range(6-i):
                        print(" ", end='')
                    print("\\", end='')
                elif j == i:
                    print("/")
                else:
                    print("::", end='')




        if i < 0:
            for j in range(0, i-1, -1):
                if j == 0:
                    for k in range(6+i):
                        print(" ", end='')
                    print("/", end='')
                elif j == i:
                    print("\\")

                else:
                    print("::", end='')
main()

