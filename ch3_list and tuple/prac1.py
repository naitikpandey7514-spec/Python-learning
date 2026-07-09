#take a five number from user and give its sum
numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

sum = 0
print("sum of five number is :")
for n in numbers:
    sum = sum + n 
print(sum)  