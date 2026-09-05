# import = imports the module (file), so we can use the things inside it.
# from = imports a specific function, variable, or class from the module.
import hello as h
from calculator import add,multiply
h.introduce()
print(add(10,5))
print(multiply(11,5))