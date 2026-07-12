#odd and even
def odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))
print(odd_even(num))