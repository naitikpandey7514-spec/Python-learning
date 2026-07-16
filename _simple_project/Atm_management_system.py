print("welcome:")
print("1. withdraw")
print("2.transfer money")
print("3.check balance")
pin = 1234
balance = 10000
choice = int(input("enter your choice(1-3):"))
if choice == 1:
    num = int(input("enter your pin:"))
    if num == pin:
        amount = int(input("enter your amount:"))
        balance = balance - amount
        print("your withdrawal amount is:",amount)
        print("your balance is:",balance)
        print("withdrawal successful!")
    else:
        print("invalid pin")
elif choice == 2:
    num1 = int(input("enter your pin:"))
    if pin == num1:
       acc = int(input("enter the receiver account number:"))
       ifsc = int(input("enter the receiver ifsc code:"))
       amount = int(input("enter the transfer amount:"))
       balance = balance - amount
       print("transfered amount is:",amount)
       print("balance is:",balance)
       print("money is transfer successfully")
    else:
        print("invalid pin:") 

elif choice == 3:
    num3 = int(input("enter your pin:"))
    if pin == num3:
        print("your account balance is:",balance)
        print("may i help you")
    else:
        print("invalid pin")
else:
    print("enter valid choice")            