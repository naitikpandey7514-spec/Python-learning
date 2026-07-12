 #oops-object oriented programming is a programming paradigm that uses objects and classes to structure code.

#class is a blueprint for creating objects. It defines the properties and behaviors that the objects created from the class will have.

#syntax
class Student:
    pass
#object is an instance of a class. It is a specific implementation of the class that has its own unique state and behavior.

#eg
class Student:
    pass

s1 = Student()
s2 = Student()

print(type(s1))

#Constructor (__init__()) - A constructor runs automatically when an object is created.

#eg
class Student:
    def __init__(self):
        print("Student object created")

s1 = Student()
