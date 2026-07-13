"""Create a class named employee having attributes -
emp_name, emp_age, and emp_city. Create a method
named get_data() in employee class that takes user input
for these attributes. Derive a class named emp_derived()
from the employee class, having an __init__() method that
displays the attributes of the employee class upon
instantiation."""

class employee:
    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = int(input("Enter salary: "))

class emp_derived(employee):
    def __init__(self):
        self.get_data()
        print("Enter employee details: ")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Salary: ", self.salary)


e = emp_derived()



