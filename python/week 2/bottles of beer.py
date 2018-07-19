def Beersong(start):
    for i in range(start, 0, -1):
        print(i,"bottels of beer on the wall,", i, "bottles of beer.\nTake one down, pass it arround", (i-1), "bottles of bear on the wall!")
def main():
    print("start us off!")
    start = int(input())
    Beersong(start)
                       
main()
