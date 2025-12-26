# addition
def add(num1, num2):
    return num1 + num2

# multiplication
def multiply(num1, num2):
    return num1 * num2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nChoose an operation:")
print("1. Addition")
print("2. Multiplication")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    result = add(num1, num2)
    print("Result of addition:", result)

elif choice == 2:
    result = multiply(num1, num2)
    print("Result of multiplication:", result)

else:
    print("Invalid choice! Please enter 1 or 2.")
