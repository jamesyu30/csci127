#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: October 19, 2023

names = input("Names: ")
name = names.split("; ")
for n in name:
    print(n.split(", ")[1], n.split(",")[0])