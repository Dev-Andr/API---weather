from turtle import Screen, Turtle
import bar, time, ball, random

s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pong")
s.tracer(0)

bar = bar.Create
p1 = bar((-350, 0))
p2 = bar((350, 0))

ball = ball.Create()
ball.setheading(45)
speed = 1
hits = 0

writer = Turtle()
writer.penup()
writer.hideturtle()
writer.color("white")
writer.setpos(0, 200)

s1, s2 = 0, 0

def score():
    writer.clear()
    writer.write(f'{s1}|{s2}', align="center", font=("Courier", 50, "normal"))

score()

def mirror():
    for t in [p1, p2]:
        if t.ycor() > 301:
            t.goto(t.xcor(), -300)
        elif t.ycor() < -301:
            t.goto(t.xcor(), 300)


s.listen()
s.onkeypress(lambda: bar.up(p1), "w")
s.onkeypress(lambda: bar.down(p1), "s")
s.onkeypress(lambda: bar.up(p2), "Up")
s.onkeypress(lambda: bar.down(p2), "Down")

while True:
    ball.fd(0.75 + 0.03 * hits)
    win = ball.bounce([p1, p2])

    if win:
        if win == "hit":
            hits += 1
            continue
        elif win == 2:
            s1 += 1
        elif win == 1:
            s2 += 1
        hits = 0
        ball.goto(0, 0)
        ball.setheading(random.choice([180, 270]) + ball.heading())
        score()

    time.sleep(0.001)
    mirror()
    s.update()

s.exitonclick()