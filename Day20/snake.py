from turtle import Screen, Turtle

STARTING_POSITION = [{"x": 0, "y": 0}, {"x": -20, "y": 0}, {"x": -40, "y": 0}]
SPEED = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_start()

    def create_start(self):
        for s in STARTING_POSITION:
            timmy = Turtle()
            timmy.penup()
            timmy.shape('square')
            timmy.color('white')
            timmy.goto(s['x'], s['y'])
            self.segments.append(timmy)

    def go(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x_value = self.segments[index - 1].xcor()
            y_value = self.segments[index - 1].ycor()

            self.segments[index].goto(x_value, y_value)

        self.segments[0].forward(SPEED)

    def up(self):
        if self.segments[0].heading() != 270:  # Prevent going directly backward
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:  # Prevent going directly backward
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:  # Prevent going directly backward
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:  # Prevent going directly backward
            self.segments[0].setheading(0)