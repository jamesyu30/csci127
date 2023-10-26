#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: October 26, 2023

def triangle(t, length):
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
        triangle(t, length/2)

def nestedTriangle(t, length):
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
            triangle(t, length/2)