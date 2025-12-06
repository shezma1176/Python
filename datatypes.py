name = "penguin"
age = 15
Is_student = True
Weight = 38.5

print("Name: ", name)
print("Type Of Name", type(name) )

print("Age: ", age)
print("Type Of Age: ", type(age))

print("Is_student: ", Is_student)
print("Type Of Is_student", type(Is_student))

print("weight: ", Weight)
print("Type Of weight", type(Weight))

print("After Type casting:")

age = str(age)
print("Type Of Age: ", type(age))

Weight = int(Weight)
print("Type Of Weight: ", type(Weight))