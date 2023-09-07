#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: September 7, 2023

import turtle

t = turtle.Turtle()
wn = turtle.Screen()

for i in range(5, 301, 5):
    t.forward(i)
    t.left(91)

wn.exitonclick()