import turtle

def draw_koch_segment(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(length, depth-1)
        turtle.left(60)
        draw_koch_segment(length, depth-1)
        turtle.right(120)
        draw_koch_segment(length, depth-1)
        turtle.left(60)
        draw_koch_segment(length, depth-1)

def draw_koch_snowflake(length, depth):
    for i in range(3):
        draw_koch_segment(length, depth)
        turtle.right(120)

turtle.speed(0)
turtle.penup()
turtle.goto(-150, 150)
turtle.pendown()

draw_koch_snowflake(300, 4)

turtle.done()
