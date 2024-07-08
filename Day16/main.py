from turtle import Turtle, Screen

myScreen = Screen()

myTurtle = Turtle()
print(myTurtle)
myTurtle.shape("turtle")
myTurtle.color("blue")
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)


print(f"{myScreen.canvheight} {myScreen.canvheight}")
myScreen.exitonclick()