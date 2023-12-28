from turtle import Turtle

class Create(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(3, 0.5)
        self.penup()
        self.goto(pos)

    def up(t):
        t.goto(t.xcor(), t.ycor() + 30)

    def down(t):
        t.goto(t.xcor(), t.ycor() - 30)
