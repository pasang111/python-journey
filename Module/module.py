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