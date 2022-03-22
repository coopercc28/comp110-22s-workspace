"""Drawing of an old box TV sitting on a table in a living room.

First, on line 26, I created a function to add a color to the background, which in this scene was a blue wall. 
Then, on line 40, I created a function in order to create the perimeter of the television and filled the color in as brown. 
On line 59, I created another function to draw the screen of the TV and filled it in with black. 
On line 74, I created a function to draw little black circles that were the volume and channel controls of an old TV.
I figured out how to draw a circle from the Turtle documentation page, which was something fun.
On line 86, I created a function to draw a table top the the TV would be sitting on, and I made the table red. 
Then, on line 104, I created a function to draw the legs of the table that the TV would be sitting on. 
On line 13, I created the main function in order to call all the functions, and put each individual function in the correct place in Turtle.
"""

__author__ = "730394353"

from turtle import Turtle, colormode, done
colormode(225)


def main() -> None:
    """The entry point of my scene."""
    friends: Turtle = Turtle()
    friends.speed(100)
    background(friends, -400, -400)
    big_box(friends, -150, -125)
    screen(friends, -145, -120)
    nobs(friends, 130, 60)
    nobs(friends, 100, 60)
    nobs(friends, 115, 25)
    top(friends, -220, -124.9)
    legs(friends, -150, -150)
    legs(friends, 150, -150)
    done()


def background(wall: Turtle, x: float, y: float) -> None:
    """The wall behind the TV."""
    wall.color("blue")
    wall.penup()
    wall.goto(x, y)
    wall.pendown()
    wall.begin_fill()
    i: int = 0
    while i < 4:
        wall.forward(800)
        wall.left(90)
        i += 1
    wall.end_fill()


def big_box(joey: Turtle, x: float, y: float) -> None:
    """The perimeter of the TV filled with brown."""
    joey.color("brown")
    joey.penup()
    joey.goto(x, y)
    joey.pendown()
    joey.begin_fill()
    joey.forward(300)
    joey.left(90)
    joey.forward(250)
    joey.left(90)
    joey.forward(300)
    joey.left(90)
    joey.forward(250)
    joey.left(90)
    joey.end_fill()


def screen(chandler: Turtle, x: float, y: float) -> None:
    """The black screen of the TV."""
    chandler.color("black")
    chandler.penup()
    chandler.goto(x, y)
    chandler.pendown()
    chandler.begin_fill()
    i: int = 0
    while i < 4:
        chandler.forward(225)
        chandler.left(90)
        i += 1
    chandler.end_fill()


def nobs(ross: Turtle, x: float, y: float) -> None:
    """The volume nob and the channel changing nobs."""
    ross.color("black")
    ross.penup()
    ross.goto(x, y)
    ross.pendown()
    ross.begin_fill()
    ross.circle(10)
    ross.end_fill()


def top(monica: Turtle, x: float, y: float) -> None:
    """The table top that the TV is going to sit on."""
    monica.color("red")
    monica.penup()
    monica.goto(x, y)
    monica.pendown()
    monica.begin_fill()
    monica.forward(440)
    monica.right(90)
    monica.forward(40)
    monica.right(90)
    monica.forward(440)
    monica.right(90)
    monica.forward(40)
    monica.end_fill()


def legs(rachel: Turtle, x: float, y: float) -> None:
    """The legs of the table the TV is sitting on."""
    rachel.color("red")
    rachel.penup()
    rachel.goto(x, y)
    rachel.pendown()
    rachel.begin_fill()
    rachel.right(90)
    rachel.forward(20)
    rachel.right(90)
    rachel.forward(150)
    rachel.right(90)
    rachel.forward(20)
    rachel.right(90)
    rachel.forward(150)
    rachel.end_fill()


if __name__ == "__main__":
    main()