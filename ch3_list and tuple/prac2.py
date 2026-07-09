# take a five number from the user and gives its multiplication

num = []
for i in range(5):
    n=int(input("enter the num:"))
    num.append(n)

mult = 1

print("multiplication of 5 number is:")
for n in num:
    mult = mult * n

print(mult)    