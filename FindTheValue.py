dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

user_input = input("Enter a key: ")

if user_input.isdigit():
    key = int(user_input)
    if key in dict:
        print("The value is:", dict[key])
    else:
        print("Key not found in the dictionary.")
else:
    print("Please enter a valid integer key (example: 4).")

