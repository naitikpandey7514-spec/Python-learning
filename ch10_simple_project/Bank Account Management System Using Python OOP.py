#BANK ACCOUNT MANAGEMENT SYSTEM

class bank_Account:

    def create_account(self):
        self.name = input("enter the name:")
        self.address = input("enter your address:")
        self.contact = int(input("enter your contact number:"))
        self.account_no = int(input("Enter Account Number: "))
        self.balance = int(input("Add money in your  account: "))

        print("Your account is created successfully")
        

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
    
    def detail(self):
        print("your name is:",self.name)
        print("your address is :",self.address)
        print("your contact number is:",self.contact)
        print("your account no is",self.account_no)
        print("your current balance is :",self.balance)

s1 = bank_Account()
s1.create_account()

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Acc_details")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        s1.debit()
    elif choice == 2:
        s1.credit()
    elif choice == 3:
        s1.account_balance()
    elif choice == 4:
        s1.detail()
    else:
        print("Invalid Choice")