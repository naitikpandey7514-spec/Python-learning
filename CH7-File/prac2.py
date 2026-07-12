#write a program to count the number of characters in a file

f = open("simple.txt", "r")
read = f.read()
count = len(read)
print("Total characters in the file:", count)
f.close()