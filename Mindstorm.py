import turtle

myTurtle = turtle.Turtle()
turtle.speed(0)
window = turtle.Screen()
window.bgcolor("red")

def draw_square ():
    for n in range (0,4):
        myTurtle.forward (100)
        myTurtle.right(90)
    


for n in range (0,360):
    draw_square()
    myTurtle.right(1)

window.exitonclick()
