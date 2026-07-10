#ascending and descending order
numbers = set()

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.add(num)

print("Original Set:", numbers)
print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))