
#take 5 students name in the file

file = open("students.txt", "w")

for i in range(5):
    name = input("Enter student name: ")
    file.write(name + "\n")

file.close()

print("Data saved successfully.")