# A nested dictionary representing employee details
employees = {
    "John": {
        "Age": 30,
        "Department": "IT"
    },
    "Sarah": {
        "Age": 28,
        "Department": "HR"
    }
}

# Access John's department
print(employees["John"]["Department"])
# Output: IT

# Update Sarah's age
employees["Sarah"]["Age"] = 29

# Add a new employee
employees["Mike"] = {
    "Age": 35,
    "Department": "Finance"
}

# Print the updated dictionary.
print(employees)
