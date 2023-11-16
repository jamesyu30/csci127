def toNum (bin):
    sum = 0
    place = 0
    for i in bin[::-1]:
        sum = sum + (int(i)*(2**place))
        place+=1
    return sum

print("num100101", toNum("100101"))
print("num1111", toNum("1111"))
print("num1010", toNum("1010"))

def toBin(num):
    place = 0
    while num % (2**place) != num:
        place+=1
    bin = "1"
    num = num - (2**(place-1))
    for i in range(place-2, -1, -1):
        if (num % (2**i) != num):
            num = num-(2**i)
            bin+="1"
        else:
            bin+="0"
    return bin

def toBin2(num):
    stri=""
    while int(num/2) != 0:
        stri+=str(num%2)
        num = int(num/2)
    stri+=str(num%2)
    return stri[::-1]

print("bin26", toBin2(26))
#print(int(1/2))
print("bin15", toBin2(15))
print("bin10", toBin(10))

def main():
     bin = input("Enter binary: ")
     print(toBin2(toNum(bin)+1))

if __name__ == "__main__":
    main()
