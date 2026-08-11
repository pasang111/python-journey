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

# This is helpful, but it can result in naming conflicts if you already have functions or variables with the same name defined in the Python script itself. So that's something to keep in mind when choosing which type of import statement you want to use.
