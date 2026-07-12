#absraction - the process of hiding the internal details of an object and showing only the necessary information to the user.

#eg

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")

c = Car()
c.start()