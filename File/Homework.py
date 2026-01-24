with open("homework.txt", "a") as file:
    n = int(input("How many homework tasks do you want to add? "))

    for i in range(n):
        subject = input("Enter subject name: ")
        task = input("Enter homework task: ")
        due_date = input("Enter due date: ")

        file.write(f"Subject: {subject} | Task: {task} | Due: {due_date}\n")

print("Homework saved successfully!")
# read_homework.py

with open("homework.txt", "r") as file:
    print("\n📚 Homework To-Do List:\n")
    print(file.read())
# homework_menu.py

while True:
    print("\n1. Add Homework")
    print("2. View Homework")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        with open("homework.txt", "a") as file:
            subject = input("Subject: ")
            task = input("Task: ")
            due = input("Due date: ")
            file.write(f"{subject} | {task} | {due}\n")
            print("Homework added!")

    elif choice == "2":
        with open("homework.txt", "r") as file:
            print("\nHomework List:")
            print(file.read())

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")