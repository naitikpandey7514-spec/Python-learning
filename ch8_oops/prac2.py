"""Write a python program to create a class named area.
Define a class method find_area() that can find areas of
different shapes whose value is given by the user. Invoke
the class method by instantiation and prove method
overloading."""

class Area:
    def find_area(self, length=None, breadth=None, radius=None):
        
        if radius is not None:
            print("Area of Circle =", 3.14 * radius * radius)

        elif length is not None and breadth is not None:
            print("Area of Rectangle =", length * breadth)

        elif length is not None:
            print("Area of Square =", length * length)

        else:
            print("Invalid Input")

a = Area()

print("1. Square")
print("2. Rectangle")
print("3. Circle")

choice = int(input("Enter your choice: "))

if choice == 1:
    side = float(input("Enter side: "))
    a.find_area(length=side)

elif choice == 2:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    a.find_area(length, breadth)

elif choice == 3:
    radius = float(input("Enter radius: "))
    a.find_area(radius=radius)

else:
    print("Invalid Choice")