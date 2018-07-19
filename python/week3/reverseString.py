def reverseone(toback):
    back = ""
    for i in range(len(toback),0,-1):
        back = back + toback[i-1]
    return back
def reverseAll(x):
    done = list(map(reverseone,x))
    return done

x = ["hello", "cello", "i'm", "mello"]
print(x)
print(reverseAll(x))

