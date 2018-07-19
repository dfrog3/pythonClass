#sum of values
#even number filter
#4 million cap
#number generator
def numCheck(num3):
    if num3 % 2 == 0:
        return num3
    return 0

num1 = 1
num2 = 2
total = 2
while 1>0:
    num3 = num1 + num2
    if num3 > 4000000:
        break
    num1 = num2
    num2 = num3
    num3 = numCheck(num3)
    total = total + num3
print(total)
