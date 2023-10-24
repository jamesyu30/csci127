#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: October 19, 2023

hour = int(input("Hour: "))

if hour < 12:
    print("Good Morning")
elif (hour < 17 and hour > 12):
    print("Good Afternoon")
else:
    print("Good Evening")