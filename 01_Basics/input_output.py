#building  a simple report card printer

name = "Alice" #declaring the variable
print(name) # printing the above name alice
print(type(name)) #type casting now to check whats the data type for the variable alice 

is_student = True # for the boolean we use true and false
print(is_student , type(is_student)) # what we did in the following line is printing the variable first and checking the datatupe in same line

print(name , type(name)) #same like first code but the thing is we print the variable and the data type in the same line

age = 29
print(age,type(age)) # normal like the above code just printing the age and its data type

score = 80.5
print(isinstance(score, float))

# isinstance() checks whether a variable belongs to a specific data type.
# Here score contains 80.5, which is a float.
# Since we are checking if score is a float, the result is True.

#one more example 
score = True
print(isinstance(score , float)) # we can see the ans is false because the datatype is bool but we checked it is float or not so it shows false

#one more example with true ans
score = 111.11
print(isinstance(score , float)) # the answer is correct because the datatype we declared is also float and we checked is it float or not it is a float


score = 11
print(isinstance(score , int))

ss = "pasang"
print(ss , type(ss) , isinstance(ss,int) ) #why false ans cause pasang is str not int

ccc = "1213"
print(isinstance(ccc , float))