                                                                # Module in Py
# in software development, a library is like a tool box for a developers.
# instead of having to implement single part of the code from the scratch ourself, a library gives you pre-written and reusable code, like functions, classes and data structure that we can use in our projects.

# Python has an extensive standard library with many different built-in modules.
# Some examples of popular built-in modules are math, random, re (short for "regular expressions"), and datetime

# The math module has helpful functions for performing more complex mathematical operations.

# The random module is helpful for generating random numbers.

# The re module is used for working with regular expressions.

# And the datetime module is helpful for working with dates and times in Python.

# But how can you access the variables, constants, functions, and classes defined in these built-in modules?

# You use an import statement. These statements let you import modules into your Python script. Import statements are generally written at the top of the file. Also, you can customize them based on your needs. First, you use the import statement, followed by the name of the module:

# import module_name    

# let's suppose we want to import math module. In this case we should write this at the top of our file:

# import math

# Then, if you need to call a function from that module in your Python script, you would use dot notation, with the name of the module followed by the name of the function:

# module_name.function_name() 

# For example, to get the square root of 36, you would write math followed by a dot and then sqrt, an abbreviation of square root, and within parentheses, you would pass any necessary arguments. In this case, we only need to pass in the number we want the square root of:

# math.sqrt(36)

# This is the most basic version of an import statement, but there are other alternatives.

# If you need to import the module with a different name (also known as an "alias"), you can use this syntax, with as followed by the alias at the end of the import statement:

# import module_name as module_alias
# This is often used to shorten long module names, or to avoid naming conflicts.

# For example, to refer to the math module as m in your code, you can assign an alias to it, like this:

# import math as m 
# Then, you can access the elements of the module using the alias:

# m.sqrt(36)
# But sometimes you don't need to import everything from a module. Perhaps you only need one or two specific functions or classes. Python has exactly what you need in that case.

# Now the import statement starts with from, followed by the name of the module, and then the import keyword followed by the name of the elements that you want to import:

# from module_name import name1, name2
# Then, you can use these names without the module prefix in your Python script.

# If you want to assign aliases to these names, you can do that by using the as keyword after each, followed by the alias you want to use:

# from module_name import name1 as alias1, name2 as alias2
# Let's say that you only want to import the radians, sine, and cosine functions from the math module. You would write:

# from math import radians, sin, cos
# Now you can call these functions directly in your code, without the math module as a prefix.

# Here we have a more detailed example:

# To find the sine and cosine of a specific angle initially expressed in degrees, we can call the radians function to convert it to radians, and then call the sine and cosine functions, passing the angle in radians:

# from math import radians, sin, cos

# angle_degrees = 40
# angle_radians = radians(angle_degrees)

# sine_value = sin(angle_radians)
# cos_value = cos(angle_radians)

# print(sine_value) # 0.6427876096865393
# print(cos_value)  # 0.766044443118978
# Notice how we are calling the functions directly, without the name of the module as a prefix. This is because we imported the functions with this alternative syntax.

# You can add this section at the end to cover module types, useful import patterns, __name__, and best practices. I’d also slightly clarify that from ... import ... can create naming conflicts.

# Additional Python Module Notes
# More About Python Modules
# Python modules are not limited to built-in modules. You can also create your own modules by putting Python code inside a .py file. Any Python file can act as a module, and you can import it into another Python file.
# For example, suppose we have a file called calculator.py:
# def add(a, b):
# return a + b
# def subtract(a, b):
# return a - b
# We can import this module into another Python file:
# import calculator
# print(calculator.add(10, 5))
# print(calculator.subtract(10, 5))
# This allows us to organize our code into separate files instead of putting everything into one large Python script.
# Python modules can generally come from three places:
# 1. The Python standard library
# 2. Third-party packages installed separately
# 3. Modules that you create yourself
# The standard library comes with Python, so modules such as math, random, datetime, os, and json can be imported without installing anything extra.
# Third-party packages are created by other developers and usually need to be installed before you can use them. Examples include requests, pandas, and numpy.
# You can also import multiple modules in the same Python file:
# import math
# import random
# import datetime
# You can use each module with dot notation:
# print(math.sqrt(25))
# print(random.randint(1, 10))
# print(datetime.datetime.now())
# You can also import multiple names from the same module:
# from math import sqrt, pi
# print(sqrt(49))
# print(pi)
# Python also provides a special __name__ variable. When a Python file is run directly, its __name__ value is "__main__". When the same file is imported as a module, its __name__ usually becomes the name of the module.
# Because of this, you will often see:
# if name == "main":
# print("This file is being run directly.")
# This is useful when you want some code to run only when the file is executed directly, but not when the file is imported into another program.
# For example:
# def greet():
# print("Hello!")
# if name == "main":
# greet()
# If we run this file directly, greet() will be called. But if another file imports this module, the greet() function will be available without automatically calling it.
# Another useful concept is the wildcard import:
# from math import *
# This imports many names from the math module directly into your program. However, this style is generally discouraged because it can make it difficult to know where a particular function or variable came from and can cause naming conflicts.
# For example, using:
# import math
# print(math.sqrt(25))
# makes it clear that sqrt() comes from the math module.
# In general, using import module_name is often a good choice because it keeps your code readable and makes the source of functions and classes obvious.
# You should also avoid giving your Python files the same names as standard library modules. For example, naming your own file random.py or math.py can cause import problems because Python may try to import your file instead of the standard library module.
# The main idea is that modules help us organize, reuse, and maintain our Python code. Instead of writing the same functionality again and again, we can place related code inside a module and import it whenever we need it.
