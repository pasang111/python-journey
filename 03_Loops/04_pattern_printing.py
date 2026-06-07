# number pattern - prints numbers in a single line from 1 to n

def number_pattern(n):

    # check if input is an integer
    if not isinstance(n, int):
        return "Argument must be an integer value"

    # check if number is greater than 0
    if n < 1:
        return "Argument must be an integer greater than 0"

    # store final result string
    pattern = ""

    # loop through numbers from 1 to n and build the pattern string
    for i in range(1, n + 1):
        # convert number to string and add space after each number
        pattern = pattern + str(i) + " "

    # remove extra space at the end
    return pattern.strip()


# test the function
print(number_pattern(4))


# pattern printing - number triangle

def number_triangle(n):

    # check if input is an integer
    if not isinstance(n, int):
        return "Argument must be an integer value"

    # check if number is valid (greater than 0)
    if n < 1:
        return "Argument must be an integer greater than 0"

    # store final pattern
    pattern = ""

    # loop for each row
    for i in range(1, n + 1):

        # build numbers for each row
        for j in range(1, i + 1):
            pattern = pattern + str(j) + " "

        # move to next line after each row
        pattern = pattern + "\n"

    # remove extra space/newline at end
    return pattern.strip()


# test the function
print(number_triangle(4))