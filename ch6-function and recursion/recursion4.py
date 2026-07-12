#power of the number

def power(a, b):
    if b == 0:
        return 1

    return a * power(a, b - 1)
n1 = int(input("Enter a number: "))
n2 = int(input("Enter the power: "))

print(power(n1, n2))