#voting eligibility

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise Exception("Not Eligible to Vote")

except Exception as e:
    print(e)

else:
    print("Eligible to Vote")

finally:
    print("Process Completed.")