import turtle

t= turtle.Turtle()
t.speed(100)
t.goto (0, 0)
t.color("light blue")

for i in range (700):
    t.forward (100+i)
    t.left(100+1)
    t.color("light blue")
    t.forward(75+i)
    t.left(100+1)
    t.color("Light pink")
turtle.exitonclick()

import turtle

t= turtle.Turtle()
t.speed(100)
t.goto (0, 0)
t.color("light purple")

for i in range (700):
    t.forward (100+i)
    t.left(100+1)
    t.color("red")
    t.forward(75+i)
    t.left(100+1)
    t.color("Light purple")
turtle.exitonclick()