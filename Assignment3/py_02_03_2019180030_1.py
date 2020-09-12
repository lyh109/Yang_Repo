import turtle
def draw_circle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(60)

def draw_ee(x, y, length):
    turtle.penup()
    turtle.goto(x, y)
    turtle.right(40)
    turtle.pendown()
    turtle.forward(30)
    turtle.right(50)
    turtle.forward(length)

def draw_line(x, y, length):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(length)
    
draw_circle(-400, 0)
draw_ee(-300, 190, 250)
turtle.left(90)

draw_circle(-100, 0)
draw_ee(0, 190, 200)

turtle.left(90)
draw_line(23, 100, 50)
draw_line(23, 30, 50)

draw_circle(-30, -150)

turtle.right(90)
draw_line(200, 190, 40)
turtle.left(90)
draw_line(120, 150, 160)

draw_circle(200, 0)

draw_line(120, -40, 200)
draw_ee(297, 190, 300)

turtle.exitonclick()
