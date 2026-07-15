#transection and deposite amount
balance = 10000

try:
    print("1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter your choice (1/2): "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")

    if choice == 1:
        balance += amount

    elif choice == 2:
        if amount > balance:
            raise Exception("Insufficient Balance")
        balance -= amount

    else:
        raise Exception("Invalid Choice")

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Transaction Failed:", e)

else:
    print("Transaction Successful")
    print("Current Balance =", balance)

finally:
    print("Thank You! Visit Again.")