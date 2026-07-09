#string method
#String methods are built-in functions used to perform operations on strings. They return a new string because strings are immutable.

#eg
txt="i aM  naiTIK 18"

print(txt.lower())        #lower()	Converts all letters to lowercase	
print(txt.upper())        #upper()	Converts all letters to uppercase	
print(txt.title())        #title()	First letter of each word becomes capital
print(txt.capitalize())   #capitalize()	Capitalizes the first letter	
print(txt.swapcase())     #swapcase()	Changes uppercase to lowercase and vice versa
print(txt.find("naiTik")) #find()  Returns the index of a substring.
print(txt.count("n"))     #count()  Counts occurrences of a substring.
print(txt.split())        #split()  Splits a string into a list.
print(txt.replace("naiTIK","pandey")) #replace()  Replaces one substring with another