# A nested dictionary representing student grades
students = {
    "Alice": {
        "Math": 92,
        "Science": 88
    },
    "Bob": {
        "Math": 85,
        "Science": 90
    }
}

# Access Alice's Science grade
print(students["Alice"]["Science"])
# Output: 88

# Update Bob's Math grade
students["Bob"]["Math"] = 89

# Add a new student
students["Charlie"] = {
    "Math": 95,
    "Science": 93
}

# Print the updated dictionary
print(students)
