file = open("students.txt", "w")

name = input("Enter student name: ")
marks = input("Enter marks: ")

file.write(f"Name: {name}, Marks: {marks}\n")

file.close()

print("Student data written successfully")