# Turtle: draw four circles
import turtle
r = eval(input("Enter radius: "))
turtle.forward(r)
turtle.pendown()
turtle.circle(r)
turtle.right(180)
turtle.circle(r)
turtle.penup()
turtle.forward(2 * r)
turtle.pendown()
turtle.circle(r)
turtle.right(180)
turtle.circle(r)