#file I/O

"""A file is used to store data permanently on your computer.
 Python provides built-in functions to create, read, write, and update files."""

#syntax to open a file in Python:

#file = open("filename.txt", "mode")

#modes of open file:

#w(write) -Opens a file for writing only; if the file exists, it will be truncated.

file = open("simple.txt", "w")
file.write("Naitik\n")
file.write("Python Learning")
file.close()

#r(read) -Opens a file for reading only; the file must already exist.

file = open("simple.txt", "r")
print(file.read())
file.close()

#a(append) -Opens a file for appending data at the end; if the file does not exist, it will be created.

file = open("simple.txt", "a")
file.write("\nWelcome")
file.close()

# x mode is use to create a new file. If the file already exists, the operation will fail.

file = open("newfile.txt", "x")
file.write("New File Created")
file.close()

#r+ (read and write) -Opens a file for both reading and writing; the file must already exist.

file = open("simple.txt", "r+")
print(file.read())
file.write("\n btech AI & ML")
file.close()

#w+ (write and read) -Opens a file for both writing and reading; creates the file if it does not exist.

file = open("simple.txt", "w+")
file.write("Python")
file.seek(0)
print(file.read())
file.close()

#a+ (append and read) -Opens a file for both appending and reading; creates the file if it does not exist.

file = open("simple.txt", "a+")
file.write("\nProgramming")
file.seek(0)
print(file.read())
file.close()