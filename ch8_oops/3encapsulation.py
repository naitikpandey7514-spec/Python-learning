
#encapsulation - it is useed to wrapping data and methods into a single class. it is used to protect the data and hides internal details from outside world and shows only necessary details to the outside world.


#eg
class Demo:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

    def show(self):
        print(self.public)  # for public
        print(self._protected)  # for protected
        print(self.__private)  # for private

d = Demo()
d.show()