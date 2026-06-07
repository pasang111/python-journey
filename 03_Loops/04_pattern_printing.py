# pattern printing - number triangle

def number_triangle(n):
    # check if input is an integer or not
    if not isinstance(n, int):
        return "Argument must be an integer value" #if the value is not instance return .......
    
    # check if number is valid (greater than 0)
    if n < 1:
        return "Arguments must be an integer greater than 0"
    
    # this will store the final pattern
    pattern = ""
    
    # loop for each row
    for i in range(1, n + 1):
        
        # build numbers for each row
        for j in range(1, i + 1):
            pattern = pattern + str(j) + " "
        
        # move to next line after each row
        pattern += "\n"

    # remove extra space/newline at end
    return pattern.strip()


# test the function
print(number_triangle(4))