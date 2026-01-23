
file = open("students.txt", "a")

n = int(input("How many students to add? "))

for i in range(n):
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    file.write(f"Name: {name}, Marks: {marks}\n")

file.close()

print("Student data appended successfully")