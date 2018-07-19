import webbrowser
import sys
import pyperclip

if len(sys.argv)>1:
    address = (sys.argv[1:])
else:
    address = pyperclip.paste()
print(address)

webbrowser.open("https://www.google.com/maps/place/"+address)
