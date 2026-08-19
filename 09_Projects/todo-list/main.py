# Create an empty list to store all our tasks
tasks = []


def add_task():
    # Ask the user to enter a task
    task = input("Enter task: ")

    # Add the task to the list with "completed" set to False
    tasks.append({"task": task, "completed": False})

    # Tell the user that the task was successfully added
    print("Task added!\n")


def view_tasks():
    # Check if there are no tasks in the list
    if not tasks:
        print("No tasks found.\n")
        return

    # Print a heading
    print("\n===== YOUR TASKS =====")

    # Loop through every task and give it a number starting from 1
    for i, task in enumerate(tasks, start=1):

        # Show ✓ if completed, otherwise show a blank space
        status = "✓" if task["completed"] else " "

        # Display the task number, status, and task name
        print(f"{i}. [{status}] {task['task']}")

    print()


def complete_task():
    # Display all current tasks
    view_tasks()

    # If there are no tasks, stop this function
    if not tasks:
        return

    try:
        # Ask the user which task they want to complete
        number = int(input("Enter task number to complete: "))

        # Check that the task number is valid
        if 1 <= number <= len(tasks):

            # Change the selected task's completed value to True
            tasks[number - 1]["completed"] = True

            # Tell the user the task is completed
            print("Task completed!\n")
        else:
            # Handle an invalid task number
            print("Invalid task number.\n")

    # Handle cases where the user enters something that isn't a number
    except ValueError:
        print("Please enter a number.\n")


def delete_task():
    # Display all current tasks
    view_tasks()

    # If there are no tasks, stop this function
    if not tasks:
        return

    try:
        # Ask the user which task they want to delete
        number = int(input("Enter task number to delete: "))

        # Check that the task number is valid
        if 1 <= number <= len(tasks):

            # Remove the selected task from the list
            deleted = tasks.pop(number - 1)

            # Show which task was deleted
            print(f"Deleted: {deleted['task']}\n")
        else:
            # Handle an invalid task number
            print("Invalid task number.\n")

    # Handle non-number input
    except ValueError:
        print("Please enter a number.\n")


# Keep the program running until the user chooses Exit
while True:

    # Display the main menu
    print("===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    # Ask the user to choose an option
    choice = input("Choose an option: ")

    # If the user chooses 1, call the add_task function
    if choice == "1":
        add_task()

    # If the user chooses 2, show all tasks
    elif choice == "2":
        view_tasks()

    # If the user chooses 3, complete a task
    elif choice == "3":
        complete_task()

    # If the user chooses 4, delete a task
    elif choice == "4":
        delete_task()

    # If the user chooses 5, exit the program
    elif choice == "5":
        print("Goodbye!")
        break  # Stop the while loop

    # If the user enters anything else
    else:
        print("Invalid option. Try again.\n")
