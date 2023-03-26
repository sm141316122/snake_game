from turtle import Turtle
position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.body = []
        self.first_body()
        self.head = self.body[0]

    def first_body(self):
        for pos in position:
            self.add_body(pos)

    def add_body(self, pos):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(pos)
        self.body.append(t)

    def extend(self):
        self.add_body(self.body[-1].position())

    def reset(self):
        for b in self.body:
            b.goto(1000, 1000)
        self.body.clear()
        self.first_body()
        self.head = self.body[0]

    def move(self):
        for num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[num - 1].xcor()
            new_y = self.body[num - 1].ycor()
            self.body[num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
