from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("yellow")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def make_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)
