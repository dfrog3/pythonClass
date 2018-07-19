file = open("readingfiles.csv","r")
fileLines = file.readlines()
total =0
for line in fileLines:
    x = line.split(",")
    for num in x:
        print()
        try:
            num = int(num)
        except:
            num = 0
        if(num % 2 ==0):
            total = total + num
print(total)


print(int("9"))