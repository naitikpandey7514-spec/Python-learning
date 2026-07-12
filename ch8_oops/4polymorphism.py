 #polymorphism - the ability of an object to take on many forms. In python, polymorphism allow functions and method to perform different actions.

#eg
class animal:
    def sound(self):
        print("Animal makes a sound")

class dog(animal):
    def sound(self):
        print("Dog barks")
class cat(animal):        
    def sound(self):
        print("Cat meows")
obj1 = dog()
obj2 = cat()
obj1.sound()
obj2.sound()


#types of polymorphism

#method overloading - it contains multiple methods with the same name but different parameters.

#eg
class add:
    def sum(self, a, b):
        return a + b
total = add()
print(total.sum(10, 20))


#operator overloading - it is a feature that allows us to define the behavior of operators for user-defined data types.

#eg

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student(80)
s2 = Student(90)

print(s1 + s2)