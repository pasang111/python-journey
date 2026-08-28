tasks = []

while True:
    print("\n TO-DO-LIST ")
    print("1. Add task")
    print("2. View task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter you choice: ")

    if choice == 1:
        task = input("Enter a task to do: ")
        task.append(task)
        print("Task added!")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i in range(len(task)):
                print(i +1, ".", tasks[i])

    elif choice == 3:
        if len(task) == 0:
            print("NO tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])

            number = int(input("enter task number to remove: "))

            if number >=1 and number <=len(tasks):
                tasks.pop(number - 1)
                print("Task removed")
            else:
                print("Invalid task number:")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choise.")