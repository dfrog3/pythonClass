import turtle
bob = turtle.Turtle()
bob.left(90)
for i in range(0,360,30):
    bob.setheading(i)
    bob.penup()
    bob.forward(100)
    bob.pendown()
    bob.forward(50)
    bob.penup()
    bob.forward(25)
    bob.stamp()
    bob.setposition(0,0)
turtle.done()

def clock():
    bob = turtle.Turtle()
    bob.left(90)
    for i in range(0, 360, 30):
        bob.setheading(i)
        bob.penup()
        bob.forward(100)
        bob.pendown()
        bob.forward(50)
        bob.penup()
        bob.forward(25)
        bob.stamp()
        bob.setposition(0, 0)
    turtle.done()