Year = int(input("Enter a year: "))

if (Year % 400 == 0) and (Year % 100 == 0):
    print("{0} is a Leap Year".format(Year))
elif (Year % 4 == 0) and (Year % 100 != 0):
    print("{0} is a Leap Year".format(Year))
else:
    print("{0} is not a Leap Year".format(Year))