students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

while True:
    print("\n--- Student Grade Manager ---")
    print("1. View all students")
    print("2. Add a student")
    print("3. Update marks")
    print("4. Search student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nStudents and Marks:")
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == "2":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added!")

    elif choice == "3":
        name = input("Enter student name: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated!")
        else:
            print("Student not found.")

    elif choice == "4":
        name = input("Enter student name: ")
        if name in students:
            print(name, "scored", students[name])
        else:
            print("Student not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
