#transection (account balance, debit and credit)


class Account:

    def details(self):
        self.account_no = int(input("Enter Account Number: "))
        self.balance = int(input("Enter Current Balance: "))

    def debit(self):
        amount = int(input("Enter Deposit Amount: "))
        self.balance += amount
        print("Amount Deposited:", amount)
        print("Total Balance:", self.balance)

    def credit(self):
        amount = int(input("Enter Withdraw Amount: "))

        if amount <= 0:
            print("Enter valid amount:.")
        elif amount > self.balance:
            print("Insufficient Balance.")
        else:
            self.balance -= amount
            print("Withdraw Amount:", amount)
            print("Remaining Balance:", self.balance)

    def account_balance(self):
        print("Account Balance:", self.balance)


s1 = Account()
s1.details()

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        s1.debit()
    elif choice == 2:
        s1.credit()
    elif choice == 3:
        s1.account_balance()
    else:
        print("Invalid Choice")