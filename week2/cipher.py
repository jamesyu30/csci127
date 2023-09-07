#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: September 7, 2023

res = input("-> ")
code = ""

for i in res:
    ascii = ord(i)+13
    if ascii > 122:
        code += chr(ascii - 26)
    else:
        code += chr(ascii)

print(code)