
#inheritance - its enable  class(child or derived) to inherit methods and properties of another class (parent or base).

#syntax
#class Parent:
    # Parent class code

#class Child(Parent):
    # Child class code

#types of inheritance

#single inheritance - when a child class inherits from a single parent class.

#eg
class parent:
    def skil(self):
        print("parent class")
class child(parent):
    def skill1(self):
        print("child class")
obj = child()
obj.skil()
obj.skill1()

#multiple inheritance - when a child class inherits from multiple parent classes.

#eg
class father:
    def skill(self):
        print("father class")
class mother:
    def skill(self):
        print("mother class")
class child(father, mother):
    def skill1(self):
        print("child class")
obj = child()
obj.skill()  # This will call the skill method from the first parent class (father)
obj.skill1()

#multilevel inheritance - when a child class inherits from a parent class, and then another child class inherits from that child class.

#eg
class grandfather:
    def house(self):
        print("grandfather house")
        
class father(grandfather):
    def car(self):
        print("father car")

class child(father):
    def bike(self):
        print("child bike")

obj = child()
obj.house()
obj.car()
obj.bike()

#hierarchical inheritance - when multiple child classes inherit from a single parent class.

#eg
class parent:
    def skill(self):
        print("parent class")

class child1(parent):
    def skill1(self):
        print("child1 class")
        self.skill()  # Call the parent class method

class child2(parent):
    def skill2(self):
        print("child2 class")
        self.skill()  # Call the parent class method

obj1 = child1()
obj2 = child2()

obj1.skill1()
obj2.skill2()

#hybrid inheritance - when a child class inherits from multiple parent classes, and those parent classes may also inherit from other classes.

#eg
class grandparent:
    def skill(self):
        print("grandparent class")

class parent1(grandparent):
    def skill1(self):
        print("parent1 class")
        self.skill()  # Call the grandparent class method

class parent2(grandparent):
    def skill2(self):
        print("parent2 class")
        self.skill()  # Call the grandparent class method

class child(parent1, parent2):
    def skill3(self):
        print("child class")
        self.skill1()  # Call the parent1 class method
        self.skill2()  # Call the parent2 class method

obj = child()
obj.skill3()
