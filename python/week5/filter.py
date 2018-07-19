results = open("results","r")
done = open("done","r")
print(done.read())
for i in results.readlines():
    if i in done.read():
        continue
    else:
        print(i)

results.close()
done.close()