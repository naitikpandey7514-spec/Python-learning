#GUESS THE NUMBER

import random

#select the mode of the game
print("1.EASY")
print("2. medium")
print("3.hard")
choice =int(input("choose the mode(1-3):"))
print("guess the number from (1-100):")
num1 = random.randint(1,100)
num2 = random.randint(1,80)
num3 = random.randint(1,50)



if choice == 1:
 print("you have 10 chance")
 for i in range(10):
     guess = int(input("guess the number:"))

     if guess == num1:
        print("you won!")
        break
     elif guess < num1:
        print("higher")
     else:
        print("lower")    
 else:
    print("you lose")
    print("the number was:",num1)  

elif choice == 2:
   print("you have 5 chance")
   for i in range(5):
     guess = int(input("guess the number:"))

     if guess == num2:
        print("you won!")
        break
     elif guess < num2:
        print("higher")
     else:
        print("lower")    
   else:
    print("you lose")
    print("the number was:",num2)  
elif choice == 3:
   print("you have 3 chance")
   for i in range(3):
     guess = int(input("guess the number:"))

     if guess == num3:
        print("you won!")
        break
     elif guess < num3:
        print("higher")
     else:
        print("lower")    
   else:
    print("you lose")
    print("the number was:",num3)
else:
   print("enter the valid choice")              