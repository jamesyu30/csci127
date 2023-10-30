#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: September 18, 2023

import turtle

msg0 = input("Enter: ")
msg1 = input("Enter: ")
msg2 = input("Enter: ")
msg3 = input("Enter: ")
msg4 = input("Enter: ")

t = turtle.Turtle()
l = [msg0, msg1, msg2, msg3, msg4]

for i in l:
    t.left(int(i))
    t.forward(100)