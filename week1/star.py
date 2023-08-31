#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: August 31, 2023
#This program draws a star

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
for i in range(5):
    t.forward(50)
    t.left(720/5)

wn.exitonclick()