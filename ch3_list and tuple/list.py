#list
'''list is a built-in mutable data type 
that can store multiple data type in a single variable'''

# Empty list
my_list = []

# List with elements
numbers = [10, 20, 30, 40]

# Mixed data types
mixed = [1, "Hello", 3.14, True]

#list method

numbers = [1, 2, 3]

numbers.append(4)      # Add element at end
numbers.insert(1, 10)  # Insert at index 1
numbers.remove(2)      # Remove value 2
numbers.pop()          # Remove last element
numbers.sort()         # Sort the list
numbers.reverse()      # Reverse the list
numbers.extend(["mango", "orange"])  # Adds multiple items

print(numbers)