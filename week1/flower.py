#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: August 31, 2023
#This program draws a flower

import turtle
wn = turtle.Screen()

t = turtle.Turtle()

for i in range(36):
    t.forward(100)
    t.left(145)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.left(135)
    t.forward(100)

wn.exitonclick()