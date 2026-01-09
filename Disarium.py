def is_disarium(num):
    digits = str(num)
    total = 0
    for i in range(len(digits)):
        total += int(digits[i]) ** (i + 1)
    return total == num

# Input from the user
number = int(input("Enter a number: "))

# Check and print result
if is_disarium(number):
    print(number, "is a Disarium Number")
else:
    print(number, "is NOT a Disarium Number")


