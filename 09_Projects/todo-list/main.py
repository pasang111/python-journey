tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added!\n")


def view_tasks():
    if not tasks:
        print("No tasks found.\n")
        return

    print("\n===== YOUR TASKS =====")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['task']}")
    print()


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task completed!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a number.\n")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted = tasks.pop(number - 1)
            print(f"Deleted: {deleted['task']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a number.\n")


while True:
    print("===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.\n")
