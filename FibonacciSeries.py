n1=int(input("Enter number of terms: "))
f1=0
f2=1
print("Fibonacci Series: ")
for i in range(n1):
    print(f1, end=" ")
    f=f1+f2
    f1=f2
    f2=f