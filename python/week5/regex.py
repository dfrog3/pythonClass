import re


def phonetest():
    regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    mo = regex.search("123-1hi23-1234hello hello helloo 321-321-4321")
    print(mo.group())

def batman():
    regex = re.compile(r"bat(man|phone|mobile|shark repelent)")
    mo = regex.findall("")
    print (mo)
batman()
None 