# Dictionary to store student names and their marks
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

# Keep showing the menu until the user chooses to exit
while True:
    # Display menu options
    print("\n--- Student Grade Manager ---")
    print("1. View all students")
    print("2. Add a student")
    print("3. Update marks")
    print("4. Search student")
    print("5. Exit")

    # Get the user's menu choice
    choice = input("Enter your choice: ")

    # Option 1: Display all students and their marks
    if choice == "1":
        print("\nStudents and Marks:")
        for name, marks in students.items():
            print(name, ":", marks)

    # Option 2: Add a new student and their marks
    elif choice == "2":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added!")

    # Option 3: Update the marks of an existing student
    elif choice == "3":
        name = input("Enter student name: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated!")
        else:
            print("Student not found.")

    # Option 4: Search for a student's marks
    elif choice == "4":
        name = input("Enter student name: ")
        if name in students:
            print(name, "scored", students[name])
        else:
            print("Student not found.")

    # Option 5: Exit the program
    elif choice == "5":
        print("Goodbye!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice.")
