import webbrowser
import os
import requests
import bs4

def download(url,savePath):
    res = requests.get(url)
    saveFile= open(savePath,"wb")
    for chunk in res:
        saveFile.write(chunk)
    saveFile.close()


thisPage = requests.get("https://xkcd.com")
while True:
    try:
        thisPage.raise_for_status()
    except:
        print(11)


    thisHTML = open("tempHTML.txt", "wb")
    for chunk in thisPage.iter_content(100000):
        thisHTML.write(chunk)
    thisHTML.close()
    thisHTML = open("tempHTML.txt", "r")
    bs4thisHTML = bs4.BeautifulSoup(thisHTML, "html.parser")
    x = bs4thisHTML.select(".comicNav li a ")[1].get("href")
    comicElem = bs4thisHTML.select('#comic img')
    comicUrl=""
    if comicElem == []:
        print("no image")
    else:
        comicUrl = 'http:' + comicElem[0].get('src')


        imageFile =("images/"+x[1:len(x)-1]+".png")
        try:
            download(comicUrl,imageFile)
        except:
            print("weird image")

    thisPage=requests.get("https://xkcd.com"+x)
    thisHTML.close()
    print(("https://xkcd.com"+x))
    if x=="#":
        break


