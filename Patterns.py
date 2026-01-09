print("Star Pattern\n")
n=int(input("Enter Rows="))
for i in range(n+1):
    for j in range(i):
        print("*", end="  ")
    print('\n')

print("Inverted pattern")
for i in range(9,1,-1):
    for j in range(i,1,-1):
        print("*", end="  ")
    print('\n')