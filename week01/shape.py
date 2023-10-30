#Name:  James Yu
#Email: james.yu66@myhunter.cuny.edu
#Date: August 29, 2023
#This program draws an octagon.

import turtle
wn = turtle.Screen()

sides = 8 #number of sides
length = 100 #side length

thomasH = turtle.Turtle()
for i in range(sides):
    thomasH.forward(length)
    thomasH.left(360/sides)

wn.exitonclick()
