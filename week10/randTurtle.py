#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: October 29, 2023

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(0,360)
  trey.right(a)