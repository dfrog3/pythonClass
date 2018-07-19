import re;

regex = re.compile(r"(?:(?:(?:Alice)|(?:Bob)|(?:Carol)|(?:BOB)) (?:(?:eats)|(?:pets)|(?:throws)|(?:EATS)) (?:(?:apples.)|(?:cats.)|(?:CATS.)|(?:Apples.)|(?:baseballs)))")


def hasKitty(word):
    regular = re.compile(r"^.*c[^ ]+t.*$")
    answer = regular.findall(word)
    if answer != []:
        return True
    else:
        return False



print(hasKitty("ct"))


regularexpresssion.sub("sometext",variable) #replaces something

