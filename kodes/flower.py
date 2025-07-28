'''import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.speed(10)

# Function to draw a petal
def draw_petal():
    pen.circle(100, 60)
    pen.left(120)
    pen.circle(100, 60)
    pen.left(120)

# Draw the flower (6 petals)
for _ in range(6):
    draw_petal()
    pen.right(60)

# Draw the stem
pen.color("green")
pen.right(90)
pen.forward(300)

# Hide turtle and finish
pen.hideturtle()
screen.mainloop()
'''
import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(5)
t.pensize(3)

# Head
t.penup()
t.goto(0, -100)
t.pendown()
t.fillcolor("tan")
t.begin_fill()
t.circle(100)
t.end_fill()

# Left ear
t.penup()
t.goto(-70, 30)
t.setheading(120)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.circle(50, 180)
t.end_fill()

# Right ear
t.penup()
t.goto(70, 30)
t.setheading(60)
t.pendown()
t.begin_fill()
t.circle(-50, 180)
t.end_fill()

# Eyes
def draw_eye(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.penup()
    t.goto(x+5, y+10)
    t.fillcolor("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

draw_eye(-35, 50)
draw_eye(35, 50)

# Nose
t.penup()
t.goto(0, 20)
t.setheading(0)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

# Mouth
t.penup()
t.goto(-20, -10)
t.setheading(-60)
t.pendown()
t.circle(20, 120)

# Hide turtle and keep window open
t.hideturtle()
turtle.done()
