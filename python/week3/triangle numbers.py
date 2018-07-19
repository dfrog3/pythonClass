

def triangle(fromusr):
    box=[]
    for i in range(1,fromusr+1):
        x = (i*(i+1))/2
        x = int(x)
        box.append(x)
    return box

print("give an int")
fromusr = int(input())
print(triangle(fromusr))

