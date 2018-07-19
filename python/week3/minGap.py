
def gap(x):
    output=[]
    for i in range(len(x)-1):
        #print(x[i])
        if x[i] > x[i+1]:
            c = (x[i])-(x[i+1])
        else:
            c = (x[i + 1]) - (x[i])
        #print(x[i],x[i+1],c)
        output.append(c)
    return output


def bubbleSort(thisList):
    for number in range(len(thisList) - 1, 0, -1):
        for i in range(number):
            if thisList[i]>thisList[i + 1]:
                jar = thisList[i]
                thisList[i] = thisList[i + 1]
                thisList[i + 1] = jar

x=[1,5,6,4,8,2,14,9,6,3,4,6,5,123,654,644,23,6,7]

step1 = list(gap(x))
#print(step1)
bubbleSort(step1)
print(step1[0])
