# 1. Creating a dictionary
# Keys are 'brand', 'model', 'year'. Their values follow the colons.
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# 2. Accessing values
# Method A: Using square brackets (Throws an error if the key doesn't exist)
brand_name = car_dict["brand"]  # Returns "Ford"

# Method B: Using .get() (Safer, returns None if the key doesn't exist)
car_color = car_dict.get("color")  # Returns None instead of crashing

# 3. Adding or Updating items
car_dict["color"] = "Red"   # Adds a new key-value pair because 'color' doesn't exist
car_dict["year"] = 2026     # Updates the value because 'year' already exists

# 4. Removing items
car_dict.pop("model")       # Removes 'model' and returns its value ("Mustang")
del car_dict["brand"]       # Deletes the 'brand' key entirely

# 5. Checking if a key exists
if "year" in car_dict:
    print("Year information is available.")

# 6. Looping through a dictionary
# Loop through keys and values simultaneously using .items()
for key, value in car_dict.items():
    print(f"{key}: {value}")
