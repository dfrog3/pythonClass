import re
userNames = ["h14","h88","h1488"]
regex = re.compile(r".*(?:(?:14)|(?:88)|(?:1488))")
out =[]
for name in userNames:
    x = regex.findall(name)
    if x !=[]:
        out.append(name)
print(out)



