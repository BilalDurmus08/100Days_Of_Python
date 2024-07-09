from turtle import Turtle, Screen

yasotaso = Turtle()
screen = Screen()
#use w a d and c for clear words for manipulate the screen

def move_forward():
    yasotaso.forward(10)


def go_backward():
    yasotaso.back(10)


def counter_clockwise():
    yasotaso.right(10)


def clockwise():
    yasotaso.left(10)


def clear():
    yasotaso.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=go_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()



