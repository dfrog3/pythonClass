#test if palendrome
#create number
def Pcheck(x):
    x=str(x)
    length = len(x)
    if length % 2 ==0:
        front = x[0:int((length/2))]
        backRaw = x[int((length/2)):length+1]
    else:
        front = x[0:int(((length-1)/2))]
        backRaw = x[(int((length-1)/2))+1:length+1]
    jar=""

    for i in range(len(backRaw)):
        toJar = int(backRaw) % 10
        backRaw = str(int(backRaw)//10)
        jar = jar + str(toJar)
    if front == jar:
        return int(x)
    else:
        return 0
swticher =True
answer = 0
for i in range(1000):
    for j in range(1000):
        num1 = i
        num2 = j
        number = num1*num2
        potent = Pcheck(number)
        if potent > answer:
            highi = i
            highj = j
            answer = potent
print(answer, highi, highj)




