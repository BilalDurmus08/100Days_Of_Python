from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)

locations = [-25, 0, 25, 50, 75, 100, 125]
colors = ["red", "purple", "blue", "orange", "grey", "black", "yellow"]
turtles = []

is_on = False

for x in range(0, 6):
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(colors[x])
    tim.goto(-220, locations[x])
    turtles.append(tim)

user_beth = screen.textinput("Beth!!", "What is your beth, give an color")

is_on = True


while is_on:
    number = random.randint(0, 5)
    number1 = random.randint(0, 10)
    turtles[number].forward(number1)
    if turtles[number].xcor() > 230:
        is_on = False
        print(f"Race is over, the winner is: {turtles[number].pencolor()}")
        if turtles[number].color() == user_beth:
            print("You won !!!1")
        else:
            print('You lost')


screen.exitonclick()
