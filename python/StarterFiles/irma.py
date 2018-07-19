import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma(x):
    """Animates the path of hurricane Irma
    """
    (bob, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here
    huricane = ("data/"+ x +".csv")
    storm = open(huricane,"r")
    stormLines = storm.readlines()
    lat = 0
    lon = 0
    wind = 0
    firstR = True
    for lines in stormLines[1:]:
        info = lines.split(",")

        lat = float(info[2])
        lon = float(info[3])
        wind = float(info[4])
        print(lat,lon,wind)




        if wind <= 74:
            bob.width(2)
            bob.color("white")
            #bob.write("0")
        elif wind >=74 and wind <=95:
            bob.width(4)
            bob.color("blue")
            bob.write("1")
        elif wind > 95 and wind <= 110:
            bob.width(6)
            bob.color("green")
            bob.write("2")
        elif wind > 110 and wind <= 129:
            bob.width(8)
            bob.color("yellow")
            bob.write("3")
        elif wind > 129 and wind <= 156:
            bob.width(8)
            bob.color("orange")
            bob.write("4")
        elif wind > 156:
            bob.width(10)
            bob.color("red")
            bob.write("5")
        bob.goto(lon,lat)







    turtle.done()


irma("irma")
