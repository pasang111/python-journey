# Import functions with aliases
from calculator import add as addition, subtract as minus

# Use the imported functions
print(addition(10, 5))
print(minus(10, 5))

# Import functions with shorter aliases
from message import welcome as start, study as learn

# Call the functions using their aliases
start()
learn()