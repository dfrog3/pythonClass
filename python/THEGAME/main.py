import pygame
from pygame.locals import *



#todo make if statement to change tiles


#todo decide winner

#todo make ai
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)


def placeTile(color,x,y):
    x,y = cordCleaner(x,y)
    pygame.draw.circle(board, color, (x, y), 10, 0)


def cordConverter(mouseX,mouseY):
    x=0
    y=0
    if mouseX <100:
        x =0
    elif mouseX>100 and mouseX<200 :
        x =1
    elif mouseX>200 and mouseX<300 :
        x =2
    elif mouseX>300 and mouseX<400 :
        x =3
    elif mouseX>400 and mouseX<500 :
        x =4
    elif mouseX>500 and mouseX<600 :
        x =5
    elif mouseX>600 and mouseX<700 :
        x =6
    elif mouseX>700 and mouseX<800 :
        x =7


    if mouseY <100:
        y =0
    elif mouseY>100 and mouseY<200 :
        y =1
    elif mouseY>200 and mouseY<300 :
        y =2
    elif mouseY>300 and mouseY<400 :
        y =3
    elif mouseY>400 and mouseY<500 :
        y =4
    elif mouseY>500 and mouseY<600 :
        y =5
    elif mouseY>600 and mouseY<700 :
        y =6
    elif mouseY>700 and mouseY<800 :
        y =7

    return x,y

def cordCleaner(mouseX,mouseY):
    if mouseX ==0:
        x =50
    elif mouseX ==1:
        x =150
    elif mouseX==2:
        x =250
    elif mouseX==3:
        x =350
    elif mouseX==4:
        x =450
    elif mouseX==5:
        x =550
    elif mouseX==6:
        x =650
    elif mouseX==7:
        x =750


    if mouseY ==0:
        y =50
    elif mouseY==1:
        y =150
    elif mouseY==2:
        y =250
    elif mouseY==3:
        y =350
    elif mouseY==4:
        y =450
    elif mouseY==5:
        y =550
    elif mouseY==6:
        y =650
    elif mouseY==7:
        y =750

    return x,y


def WhatsTheTile(mouseX,mouseY,listBoard):
    return listBoard[mouseX][mouseY]


def ListOfTiles(mouseX,mouseY,checkingTiles):


    checkingTiles.append(WhatsTheTile(mouseX,mouseY,listBoard))

def tileFlipperBoolean(color,mouseX,mouseY, listBoard):
    # south
    indexer = 0
    checkingTiles = []
    MadeASwitch = False
    waitwaitwait = False
    for i in range(mouseY, 8, 1):
        try:
            if WhatsTheTile(mouseX, i, listBoard) == '':
                break
            else:
                ListOfTiles(mouseX, i, checkingTiles)
        except:
            break
    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:
            for j in range(i + 1):
                checkingTiles[j] = color
            break
    for i in range(mouseY, 8, 1):

        try:
            if waitwaitwait and listBoard[mouseX][i] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[mouseX][i] == checkingTiles[indexer]:
                waitwaitwait = True

            indexer += 1
        except:
            break
    print("south", MadeASwitch)
    waitwaitwait = False
    indexer = 0
    checkingTiles = []

    # north
    for i in range(mouseY, -8, -1):
        try:
            if WhatsTheTile(mouseX, i, listBoard) == '':
                break
            else:
                ListOfTiles(mouseX, i, checkingTiles)
        except:
            break
    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:
            for j in range(i + 1):
                checkingTiles[j] = color
            break
    for i in range(mouseY, -8, -1):

        try:
            if waitwaitwait and listBoard[mouseX][i] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[mouseX][i] == checkingTiles[indexer]:
                waitwaitwait = True

            indexer += 1
        except:
            break
    print("north", MadeASwitch)

    # east
    waitwaitwait = False
    indexer = 0
    checkingTiles = []
    for i in range(mouseX, 8, 1):
        try:
            if WhatsTheTile(i, mouseY, listBoard) == '':
                break
            else:
                ListOfTiles(i, mouseY, checkingTiles)
        except:
            break
    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:
            for j in range(i + 1):
                checkingTiles[j] = color
            break
    for i in range(mouseX, 8, 1):

        try:
            if waitwaitwait and listBoard[i][mouseY] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[i][mouseY] == checkingTiles[indexer]:
                waitwaitwait = True

            indexer += 1
        except:
            break

    print("east", MadeASwitch)
    # west
    waitwaitwait = False
    indexer = 0
    checkingTiles = []
    for i in range(mouseX, -8, -1):
        try:
            if WhatsTheTile(i, mouseY, listBoard) == '':
                break
            else:
                ListOfTiles(i, mouseY, checkingTiles)
        except:
            break
    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:

            for j in range(i + 1):
                checkingTiles[j] = color
            break
    for i in range(mouseX, -8, -1):

        try:
            if waitwaitwait and listBoard[i][mouseY] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[i][mouseY] == checkingTiles[indexer]:
                waitwaitwait = True

            indexer += 1
        except:
            break

    print("west", MadeASwitch)

    # north West
    waitwaitwait = False
    indexer = 0
    checkingTiles = []

    y = mouseY
    for i in range(mouseX, -8, -1):

        try:
            if WhatsTheTile(i, y, listBoard) == '':
                break
            else:
                ListOfTiles(i, y, checkingTiles)
        except:
            break
        y -= 1

    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:

            for j in range(i + 1):
                checkingTiles[j] = color
            break

    y = mouseY
    for i in range(mouseX, -8, -1):

        try:
            if waitwaitwait and listBoard[i][y] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[i][y] == checkingTiles[indexer]:
                waitwaitwait = True


            indexer += 1
        except:
            break
        y -= 1

    print("nw", MadeASwitch)

    # north east
    waitwaitwait = False
    indexer = 0
    checkingTiles = []

    y = mouseY
    for i in range(mouseX, -8, -1):

        try:
            if WhatsTheTile(i, y, listBoard) == '':
                break
            else:
                ListOfTiles(i, y, checkingTiles)
        except:
            break
        y += 1

    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:
            for j in range(i + 1):
                checkingTiles[j] = color
            break

    y = mouseY
    for i in range(mouseX, -8, -1):

        try:
            if waitwaitwait and listBoard[i][y] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[i][y] == checkingTiles[indexer]:
                waitwaitwait = True

            indexer += 1
        except:
            break
        y += 1

    print("ne", MadeASwitch)

    # south east
    waitwaitwait = False
    indexer = 0
    checkingTiles = []

    y = mouseY
    for i in range(mouseX, 8, 1):

        try:
            if WhatsTheTile(i, y, listBoard) == '':
                break
            else:
                ListOfTiles(i, y, checkingTiles)
        except:
            break
        y += 1

    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:
            for j in range(i + 1):
                checkingTiles[j] = color
            break

    y = mouseY
    for i in range(mouseX, 8, 1):

        try:
            if waitwaitwait and listBoard[i][y] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[i][y] == checkingTiles[indexer]:
                waitwaitwait = True

            indexer += 1
        except:
            break
        y += 1

    print("south east", MadeASwitch)

    # south west
    waitwaitwait = False
    indexer = 0
    checkingTiles = []

    y = mouseY
    for i in range(mouseX, 8, 1):

        try:
            if WhatsTheTile(i, y, listBoard) == '':
                break
            else:
                ListOfTiles(i, y, checkingTiles)
        except:
            break
        y -= 1

    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:
            for j in range(i + 1):
                checkingTiles[j] = color
            break

    y = mouseY

    for i in range(mouseX, 8, 1):

        try:
            if waitwaitwait and listBoard[i][y] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[i][y] == checkingTiles[indexer]:
                waitwaitwait = True

            indexer += 1
        except:
            break
        y -= 1

    print("south west", MadeASwitch)

    indexer = 0
    checkingTiles = []
    waitwaitwait = False

    return MadeASwitch



def tileFlipper(color,mouseX,mouseY, listBoard):
    #south
    indexer = 0
    checkingTiles = []
    MadeASwitch = False
    waitwaitwait = False
    for i in range(mouseY,8,1) :
        try:
            if WhatsTheTile(mouseX,i,listBoard) == '':
                break
            else:
                ListOfTiles(mouseX,i,checkingTiles)
        except:
            break
    for i in range(1,len(checkingTiles)):
        if checkingTiles[0]!= color:
            break
        if checkingTiles[i]== color:
            for j in range(i+1):

                checkingTiles[j]= color
            break
    for i in range(mouseY,8,1):

        try:
            if waitwaitwait and listBoard[mouseX][i] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[mouseX][i] == checkingTiles[indexer]:
                waitwaitwait = True
            listBoard[mouseX][i]= checkingTiles[indexer]
            indexer +=1
        except:
            break
    print("south",MadeASwitch)
    waitwaitwait = False
    indexer = 0
    checkingTiles = []

    #north
    for i in range(mouseY,-8,-1) :
        try:
            if WhatsTheTile(mouseX,i,listBoard) == '':
                break
            else:
                ListOfTiles(mouseX,i,checkingTiles)
        except:
            break
    for i in range(1,len(checkingTiles)):
        if checkingTiles[0]!= color:
            break
        if checkingTiles[i]== color:
            for j in range(i+1):

                checkingTiles[j]= color
            break
    for i in range(mouseY,-8,-1):

        try:
            if waitwaitwait and listBoard[mouseX][i] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[i][mouseY] == checkingTiles[indexer]:
                waitwaitwait = True
            listBoard[mouseX][i]= checkingTiles[indexer]
            indexer +=1
        except:
            break
    print("north", MadeASwitch)

    #east
    waitwaitwait = False
    indexer = 0
    checkingTiles = []
    for i in range(mouseX, 8, 1):
        try:
            if WhatsTheTile(i,mouseY,listBoard) == '':
                break
            else:
                ListOfTiles(i,mouseY,checkingTiles)
        except:
            break
    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:
            for j in range(i + 1):
                checkingTiles[j] = color
            break
    for i in range(mouseX, 8, 1):

        try:
            if waitwaitwait and listBoard[i][mouseY] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[i][mouseY] == checkingTiles[indexer]:
                waitwaitwait = True
            listBoard[i][mouseY] = checkingTiles[indexer]
            indexer += 1
        except:
            break

    print("east", MadeASwitch)
    #west
    waitwaitwait = False
    indexer = 0
    checkingTiles = []
    for i in range(mouseX, -8, -1):
        try:
            if WhatsTheTile(i,mouseY,listBoard) == '':
                break
            else:
                ListOfTiles(i,mouseY,checkingTiles)
        except:
            break
    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:

            for j in range(i + 1):
                checkingTiles[j] = color
            break
    for i in range(mouseX, -8, -1):

        try:
            if waitwaitwait and listBoard[i][mouseY] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[i][mouseY] == checkingTiles[indexer]:
                waitwaitwait = True
            listBoard[i][mouseY] = checkingTiles[indexer]
            indexer += 1
        except:
            break

    print("west", MadeASwitch)

    #north West
    waitwaitwait = False
    indexer = 0
    checkingTiles = []

    y = mouseY
    for i in range(mouseX,-8,-1):

        try:
            if WhatsTheTile(i, y, listBoard) == '':
                break
            else:
                ListOfTiles(i, y, checkingTiles)
        except:
            break
        y -= 1

    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:

            for j in range(i + 1):
                checkingTiles[j] = color
            break

    y = mouseY
    for i in range(mouseX,-8,-1):

        try:
            if waitwaitwait and listBoard[i][y] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[i][y] == checkingTiles[indexer]:
                waitwaitwait = True

            listBoard[i][y] = checkingTiles[indexer]
            indexer += 1
        except:
            break
        y-=1

    print("nw",MadeASwitch)


    # north east
    waitwaitwait = False
    indexer = 0
    checkingTiles = []

    y = mouseY
    for i in range(mouseX, -8, -1):

        try:
            if WhatsTheTile(i, y, listBoard) == '':
                break
            else:
                ListOfTiles(i, y, checkingTiles)
        except:
            break
        y += 1

    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:
            for j in range(i + 1):
                checkingTiles[j] = color
            break

    y = mouseY
    for i in range(mouseX, -8, -1):

        try:
            if waitwaitwait and listBoard[i][y] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[i][y] == checkingTiles[indexer]:
                waitwaitwait = True
            listBoard[i][y] = checkingTiles[indexer]
            indexer += 1
        except:
            break
        y += 1

    print("ne", MadeASwitch)

    # south east
    waitwaitwait = False
    indexer = 0
    checkingTiles = []

    y = mouseY
    for i in range(mouseX, 8, 1):

        try:
            if WhatsTheTile(i, y, listBoard) == '':
                break
            else:
                ListOfTiles(i, y, checkingTiles)
        except:
            break
        y += 1

    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:
            for j in range(i + 1):
                checkingTiles[j] = color
            break

    y = mouseY
    for i in range(mouseX, 8, 1):

        try:
            if waitwaitwait and listBoard[i][y] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[i][y] == checkingTiles[indexer]:
                waitwaitwait = True
            listBoard[i][y] = checkingTiles[indexer]
            indexer += 1
        except:
            break
        y += 1

    print("south east", MadeASwitch)

    # south west
    waitwaitwait = False
    indexer = 0
    checkingTiles = []

    y = mouseY
    for i in range(mouseX, 8, 1):

        try:
            if WhatsTheTile(i, y, listBoard) == '':
                break
            else:
                ListOfTiles(i, y, checkingTiles)
        except:
            break
        y -= 1

    for i in range(1, len(checkingTiles)):
        if checkingTiles[0] != color:
            break
        if checkingTiles[i] == color:
            for j in range(i + 1):
                checkingTiles[j] = color
            break

    y = mouseY

    for i in range(mouseX, 8, 1):

        try:
            if waitwaitwait and listBoard[i][y] != checkingTiles[indexer]:
                MadeASwitch = True
            if listBoard[i][y] == checkingTiles[indexer]:
                waitwaitwait = True
            listBoard[i][y] = checkingTiles[indexer]
            indexer += 1
        except:
            break
        y -= 1

    print("south west", MadeASwitch)







    indexer = 0
    checkingTiles = []
    waitwaitwait = False

    return MadeASwitch

























pygame.init()
board = pygame.display.set_mode((800, 800))
board.fill(GREEN)
pygame.draw.line(board, BLACK, (0, 0), (0, 800), 10)
pygame.draw.line(board, BLACK, (100, 0), (100, 800), 10)
pygame.draw.line(board, BLACK, (200, 0), (200, 800), 10)
pygame.draw.line(board, BLACK, (300, 0), (300, 800), 10)
pygame.draw.line(board, BLACK, (400, 0), (400, 800), 10)
pygame.draw.line(board, BLACK, (500, 0), (500, 800), 10)
pygame.draw.line(board, BLACK, (600, 0), (600, 800), 10)
pygame.draw.line(board, BLACK, (700, 0), (700, 800), 10)
pygame.draw.line(board, BLACK, (800, 0), (800, 800), 10)

pygame.draw.line(board, BLACK, (0, 100), (800, 100), 10)
pygame.draw.line(board, BLACK, (0, 200), (800, 200), 10)
pygame.draw.line(board, BLACK, (0, 300), (800, 300), 10)
pygame.draw.line(board, BLACK, (0, 400), (800, 400), 10)
pygame.draw.line(board, BLACK, (0, 500), (800, 500), 10)
pygame.draw.line(board, BLACK, (0, 600), (800, 600), 10)
pygame.draw.line(board, BLACK, (0, 700), (800, 700), 10)
pygame.draw.line(board, BLACK, (0, 800), (800, 800), 10)

listBoard =[["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","",BLACK,WHITE,"","",""],["","","",WHITE,BLACK,"","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""]]

mouseX = 0
mouseY = 0
TURN = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            mouseX,mouseY = event.pos
            mouseX,mouseY= cordConverter(mouseX,mouseY)
            print(mouseX,mouseY)
            if listBoard[mouseX][mouseY] =="":
                if TURN:
                    listBoard[mouseX][mouseY] = WHITE
                    if tileFlipperBoolean(WHITE, mouseX, mouseY, listBoard):
                        tileFlipper(WHITE, mouseX, mouseY, listBoard)
                        TURN= False
                    else:
                        listBoard[mouseX][mouseY] = ""
                else:
                    listBoard[mouseX][mouseY] = BLACK
                    if tileFlipperBoolean(BLACK, mouseX, mouseY, listBoard):
                        tileFlipper(BLACK, mouseX, mouseY, listBoard)
                        TURN = True
                    else:
                        listBoard[mouseX][mouseY] = ""

        for i in range(8):
            for j in range(8):
                if listBoard[i][j]!= "":
                    placeTile(listBoard[i][j],i,j)

        pygame.display.flip()



