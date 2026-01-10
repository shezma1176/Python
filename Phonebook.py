phonebook = []

def add_contact():
    name = input("Enter Name: ")
    number = input("ENter Number: ")
    phonebook.append([name, number])
    print("Contact added succesfully\n")

def view_contacts():
    if phonebook == []:
        print("Phonebook is empty\n")
    else:
        print("\n ---- Phonebook Numbers ----")
        for i in range(len(phonebook)):
            print(i + 1, ".", phonebook[i][0], "-", phonebook[i][1])
            print()

def edit_contacts():
    view_contacts()
    if phonebook != []:
        index = int(input("Enter Number to Edit: ")) - 1
        if index >=0 and index < len(phonebook):
            phonebook[index][0] = input("Enter new Name: ")
            phonebook[index][1] = input("Enter new Number: ")
            print("Contact updated succesfully\n")
        else:
             print("Invalid Choice\n")

def delete_contacts():
    view_contacts()
    if phonebook != []:
        index = int(input("Enter Contact Number to Delete: ")) - 1
        if index >= 0 and index < len(phonebook):
            phonebook.pop(index)
            print("Contact deleted succesfully\n")
        else:
             print("Invalid Choice\n")

while True:
    print("📞 PHONEBOOK MENU")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        edit_contacts()
    elif choice == "4":
        delete_contacts()
    elif choice == "5":
        print("Exiting Phonebook. Goodbye 👋")
        break
    else:
        print("invalid option. Please try again\ne")
