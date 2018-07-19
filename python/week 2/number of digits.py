def digits():
    print("give me an int")
    ourInt = input()
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
    print(answer)








digits()