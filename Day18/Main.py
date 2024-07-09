from turtle import Turtle, Screen
import random

kapopo = Turtle()
kapopo.shape("circle")
kapopo.shapesize(0.5)

# creating square
# kapopo.forward(50)
# kapopo.left(90)
# kapopo.forward(50)
# kapopo.left(90)
# kapopo.forward(50)
# kapopo.left(90)
# kapopo.forward(50)

#creating dashed line
# for x in range(15):
#     kapopo.color("white")
#     kapopo.forward(10)
#     kapopo.color("black")
#     kapopo.forward(10)

# for x in range(15):
#     kapopo.pendown()
#     kapopo.forward(10)
#     kapopo.penup()
#     kapopo.forward(10)


#creating shapes
# for x in range(4, 9):
#     for n in range(x):
#         ic_aci = (x - 2) * 180 / x
#         kapopo.forward(100)
#         kapopo.left(180-ic_aci)




#Random movement picker
def direction_picker(direction_way, turtle):
    if direction_way == "right":
        turtle.right(90)
    elif direction_way == "left":
        turtle.left(90)


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = ["right", "left", "none"]
#random walk
while True:
    kapopo.forward(10)
    color = random.choice(colours)
    direction = random.choice(directions)
    kapopo.color(color)
    direction_picker(direction, kapopo)


screen = Screen()
screen.exitonclick()