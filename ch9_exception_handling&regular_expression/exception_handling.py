
# exception handling - exception handling is a mechanism  use to handle runtime errors soo the program doesnt crash and run normally. 

# we use try,except,finally,else and raise block to handle exceptions in python.

# try block - all the risky code write inside the try block that may cause an error
# except block - if any error occurs in the try block then it will be handled by the except block and the program will not crash.
# else blocl - The else block runs only if no exception occurs.
# finally block - the code inside the finally block will be executed no matter what whether an exception occurs or not.
# raise block - The raise keyword is used to create an exception

# syntax of try and except block

"""
try:
    # risky code
    pass
except:
    # handle the exception
    pass
else:
    #if no exception occur    
finally:
      #code    
"""

#example of exception handling

try :
    n1 = 5
    n2 = 5
    result = n1/n2
except ZeroDivisionError:
    print("Division by zero is not possible")
else:
    print("successful")
finally:
    print("program end")  


    #built in exception 

    # ZeroDivisionError - divide by zero is not define so python raise exception

    # ValueError - when user use invalid value
    
    # IndexError - when user find list element by its indexing which is out of range

    # TypeError - when the user use wrong data type

    # NamingError - when the variable or function doesnt defined
         



