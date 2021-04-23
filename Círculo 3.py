import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('cyan')
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()

a = 0
b = 0

while True:
    t.forward(a)
    t.right(b)
    a = a + 3
    b = b + 1
    if b==210:
        break
    t.hideturtle()

turtle.done()
s.exitonclick()