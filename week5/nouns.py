#Name:  James Yu
#Email:  james.yu66@myhunter.cuny.edu
#Date: September 26, 2023

msg = input("Nouns: ")

nounlist = msg.split(" ")
count = 0
for i in nounlist:
    if i[-1] == 's':
        count+=1
print(len(nounlist))
print(count/len(nounlist))