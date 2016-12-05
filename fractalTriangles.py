import turtle

myTurtle = turtle.Turtle()


def draw_triangle(size):
    for i in range (0,3):
        myTurtle.forward(size)
        myTurtle.left(120)

def draw_fractal(size, n):
    if (n==0):
        return

    myTurtle.left(30)

    for i in range (0,3):

        myTurtle.forward(size/4)
        myTurtle.left(90)
        draw_fractal(size/2, n-1)
        myTurtle.right(90)
        myTurtle.forward(size/4)
        myTurtle.right(120)

    #always end at 90 degrees
    myTurtle.left(330)
    

def draw_art(size, numTriangles):
    myTurtle.speed("fastest")
    window = turtle.Screen()
    window.bgcolor("blue")

    #always draw in the centre
    myTurtle.penup()
    myTurtle.sety(size/2)
    myTurtle.pendown()

    #draw first triangle facing down
    myTurtle.right(120)
    draw_triangle(size)

    #move to the bottom and face upwards because fractals are facing up
    myTurtle.left(60)
    myTurtle.forward(size)
    myTurtle.right(120)
    myTurtle.forward(size/2)

    #always start at 90 degrees (facing upwards)
    myTurtle.right(90)
    draw_fractal(size, numTriangles)
    
    window.exitonclick()


draw_art(200, 3)
