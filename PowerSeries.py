n = int(input("Enter number of terms: "))

for i in range(1, n + 1):
    value = i ** i
    if i == 1:
        value = -value
    print(value)