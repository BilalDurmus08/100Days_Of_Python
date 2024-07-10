from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0) #this added to the snake continuously movement

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_ture = True
while is_ture:
    time.sleep(0.1)
    screen.update()
    snake.go()

    if snake.segments[0].distance(food) < 12:
        print("nom nom nomm")
        food.refresh()
        scoreboard.increase_score()









screen.exitonclick()
