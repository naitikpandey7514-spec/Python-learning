#loops- A loop is used to repeat the same block of code multiple times without writing it again and again.

#Suppose you want to print Hello 5 times.
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

#some work can be done using loops instead of writing the same code again and again.

for i in range(5):
    print("hello")



    #there are two types of loops in python
     
     #1. for loop - for loop is used to executes block of code as a specified number of times.user knows how many times the  block of code runs.

     #syntax of for loop

     #for variable in sequence:
            #body of for loop

     #example
for i in range(1,5):
    print(i)


    #2. while loop - while loop is used to executes block of code as long as the condition is true.user does not know how many times the block of code runs.
    #syntax of while loop
    #while condition:
    #    body of while loop
    #example
i = 1
while i <= 5:
    print(i)
    i += 1   