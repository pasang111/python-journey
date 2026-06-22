#converting celcius to fahrenheit 

def convert_temperature(celsius):
    return (celsius + 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = convert_temperature(celsius)
print("Temperature in fahrenheit:", fahrenheit) #printing the msg