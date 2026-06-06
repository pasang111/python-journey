                                        #so what is a function?
#a function is a resuable piece of code that runs when we call it

def greet(): #def is used to define or create a function
    message = "Hello Learners" # creating a local variable inside the function
    print(message) # printing the message 

greet() # calling the function so the code inside it runs

# so what are parameters?
#parameters are variables created inside a function.
#They act as place holders for values we pass later.

def greet_user(name):
#so the name inside the greeet_user is a parameter which receives the value passed while calling the function
    print("Hello", name)

greet_user("Ace")#so here the name "Ace" is passed to the parameter name

            #NOTE :
            # print() displayes the output on the screen 
            # return sends a result back to the program


def add(a,b):
    #so in the above code a and b are parameters
    #return sends answer back to wherever the function was called
    return a+b

#calling the function and storing the returned value in the result
result = add(10,20)

#and finally printing the value stored in result
print(result)

#so now we have already printed the result once.
#what if we want to use the function again with the different values?
#we can simply call the function again and pass new arguments.

add(20,30)
#so here we called the function but if we only call add(20,20), pythin calcutes the answer
#but it will not show the answer in the screen.

#to see the result, we use print()

print(add(20,30))

#so here a = 20, and b = 30
#the functions returns 40
#print() then displays 40 on the screen
