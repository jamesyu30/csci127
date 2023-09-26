#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: September 20, 2023

msg = input("Enter: ")
for i in range(len(msg)):
    print(msg[:i])
for j in range(len(msg)):
    print(msg[j:])