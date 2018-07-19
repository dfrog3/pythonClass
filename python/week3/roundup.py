theList = [1,2,3,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2]
def roundAllUp(theList):
    box = list(map(round, theList))
    return box
box = roundAllUp(theList)
print(box)