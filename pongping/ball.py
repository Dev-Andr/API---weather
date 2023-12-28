from turtle import Turtle

class Create(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def bounce(self, p12):
        for t in p12:
            if abs(t.xcor() - self.xcor()) <= 10 and abs(t.ycor() - self.ycor()) <= 45:
                self.setheading(90 + self.heading())
                return "hit"

        if self.ycor() > 285 or self.ycor() < -285:
            self.setheading(90 + self.heading())
            return

        if self.xcor()>400:
            return 2
        elif self.xcor()<-400:
            return 1