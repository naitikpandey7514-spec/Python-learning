#example-write a python program to take a character as input from user and count the number of times that character is present in the file.


f = open("newfile.txt", "r")
ch = input("Enter a character to count: ")
data = f.read()
count = data.count(ch)
if count > 0:
    print("total count of character", ch, "is:", count)
else:
    print("character not found")    
f.close()    