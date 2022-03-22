from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()
i: int = 0
leo.penup()
leo.goto(-150, -60)
leo.pendown()
colormode(225)
leo.color("blue")

while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.goto(-150, -60)
leo.begin_fill()
# code for shape to be filled
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")
leo.end_fill()

done()

bob: Turtle = Turtle()
side_length: int = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
done()