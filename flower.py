import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
flower = turtle.Turtle()
flower.speed(15)

# Function to draw a petal
def draw_petal(color):
    flower.color(color)
    flower.begin_fill()
    flower.circle(15, 220)
    flower.left(90)
    flower.circle(30, 85)
    flower.left(85)
    flower.end_fill()

# Function to draw the flower
def draw_flower():
    flower.penup()
    flower.goto(37, -0)
    flower.pendown()
    for _ in range(6):
        draw_petal("red")
        flower.right(60)

# Draw stem
flower.color("green")
flower.penup()
flower.goto(0, -90)
flower.pendown()
flower.pensize(8)
flower.left(90)
flower.forward(95)

# Draw the flower
draw_flower()

# Hide the turtle and finish
flower.hideturtle()
turtle.done()
