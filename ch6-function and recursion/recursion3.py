#sum of the numbers

def total(n):
    if n == 1:
        return 1

    return n + total(n - 1)
num = int(input("Enter a number: "))

print(total(num))