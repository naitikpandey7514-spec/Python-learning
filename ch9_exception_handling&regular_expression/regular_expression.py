
#regular expression - it is a sequence of character used to searching text , matching pattern , validating data and spliting text.

#common regex pattern

# .(dot) - match single text , except new line
# *(star) - match zero or more occurence of specified character
# +(plus) - match one or more occurence of specified character
# ?(mark) - match zero or one occurence of specified character
# ^(caret) - matching starting of string
# $(dollar) - matching ending of string
# \d - match digit(0-9)
#\D - match non digit
#{n} - match exactly n occurence
#{n,m} - match Between n and m occurrences

# re module function

#1 re.match() - it is use to whether the pattern match at beginning of string . if match it gives match object other wise none.

#syntax-

# re.match("pattern", "string")

#eg
import re

text = "Python is easy"

result = re.match("Python", text)

if result:
    print("Match Found")
else:
    print("No Match")

#2 # re.search() - it is use to search the first occurence of the pattern in the string.it does not need started from the beginning.

#syntax-

# re.search("pattern", "string")

#eg
import re

text = "I am learning Python"

result = re.search("Python", text)

if result:
    print("Found")
    print(result.group())
else:
    print("Not Found")

#3 re.findall() - it searched all the occurences of the pattern in the string

#syntax

# re.findall("pattern", "string")

#eg

import re

text = "cat bat mat cat"

result = re.findall("cat", text)

print(result)

#4 re.split() - splits a string wherever the given pattern matches and returns the result as a list.

#syntax

# re.split(pattern, string)

#eg

import re

text = "Apple,Banana,Mango"

result = re.split(",", text)

print(result)
