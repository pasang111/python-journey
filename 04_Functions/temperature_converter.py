# Function to convert Celsius to Fahrenheit
def convert_temperature(celsius):
    return (celsius * 9/5) + 32  # Apply the conversion formula

# Get the temperature in Celsius from the user
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = convert_temperature(celsius)

# Display the converted temperature
print("Temperature in Fahrenheit:", fahrenheit)
