# Create a class called Planet
class Planet:

    # Initialize a new Planet object
    def __init__(self, name, planet_type, star):

        # Check if all arguments are strings
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            # Raise an error if any argument is not a string
            raise TypeError("name, planet_type, and star must be strings")

        # Check if any argument is an empty string
        if name == "" or planet_type == "" or star == "":
            # Raise an error if any argument is empty
            raise ValueError("name, planet_type, and star must be non-empty strings")

        # Store the planet name
        self.name = name

        # Store the planet type
        self.planet_type = planet_type

        # Store the star name
        self.star = star

    # Create a method that describes the planet's orbit
    def orbit(self):
        # Return a message showing which star the planet orbits
        return f'{self.name} is orbiting around {self.star}...'

    # Define how the Planet object should look when printed
    def __str__(self):
        # Return the planet's information as a string
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'


# Create the first Planet object
planet_1 = Planet("Mercury", "Terrestrial", "Sun")

# Create the second Planet object
planet_2 = Planet("Jupiter", "Gas Giant", "Sun")

# Create the third Planet object
planet_3 = Planet("Neptune", "Ice Giant", "Sun")


# Print the name of the first planet
print(planet_1.name)

# Print the type of the first planet
print(planet_1.planet_type)

# Print the star of the first planet
print(planet_1.star)


# Print the name of the second planet
print(planet_2.name)

# Print the type of the second planet
print(planet_2.planet_type)

# Print the star of the second planet
print(planet_2.star)


# Print the name of the third planet
print(planet_3.name)

# Print the type of the third planet
print(planet_3.planet_type)

# Print the star of the third planet
print(planet_3.star)


# Print the orbit message for the first planet
print(planet_1.orbit())

# Print the orbit message for the second planet
print(planet_2.orbit())

# Print the orbit message for the third planet
print(planet_3.orbit())


# Print the first planet using the __str__ method
print(planet_1)

# Print the second planet using the __str__ method
print(planet_2)

# Print the third planet using the __str__ method
print(planet_3)
