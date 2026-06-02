#now we are in day one and we will learn about the string how do we do it and how do we declare it
#in python we use the single and double quotes as same for example
p = "pasang"
q = 'pasamg'
print(p , q) # from this example we can see that the quotes dosent matter even though it has one or 2 quotes

#now if we want to write string in differeent line we use 3quotes for example

e = """
sodfnsdf
sdfsdf
sdfsd
fs
dfsd

"""
print(e)
# so from the above example we can see how to write multiple string


#now sometimes we need to check if a string cohntains one or more than more character. to check that we use in operator for example
f = 'Hello world'
print('hello' in f) #False
print('Hello' in f) #true
print('f' in f) #False
print('rld' in f) #true
print('d' in f) #true
print('Hell' in f) #true
print('w' in f) #true
#so now what we did in the above code was that we use in operator which helped to check is that word or alphabet in that string or not 
#like we print f and used operator and searched f it shows false because in hello world there is no any word like f and for hello also we can
# see that one hello is true while another is false why cause its casesensitive we can see in variable f h is capital letter not small so
# when we checked the hello should be in capital Hello that why lets go with another example 
text = "Python Programming"

print('Python' in text) #true
print('python' in text) #false case sensitive
print('gram' in text) #true in programming gram
print('Pro' in text) # true in progra 
print('z' in text) # false no z in the word

#last one example
pa = "pasang lama"
print('pasa' in pa) # true
print('Lama' in pa) #false  uppercase l is not there only lower case is there so
print('anG' in pa)#false
print('lama' in pa) #true
print('pasanglama' in pa)#false space lacking

# !!!!!!!!!!!!! note : while printing always put the declare variable name like print('pasang'  in pa)

#now checking the length
p = "pasang lama is a good boy in the class"
print(len(p)) #38 use len operator for printing the length of the character
#!!!!!!!!!! note space also counts here



#about indexing like for example there is world acegaming looking from first a is not 1 it is 0 we count like this and looking from back
#gaming g is -1 we point it like this in python
#for example

d = "Sakalaka boom"
print(d[0:7:1]) #0 is S and 7 means upto which character like 7 is a but we are printing k but k is 6 why we wrote 7 we need to step one step
#ahead so and what is 1 in the last go 1 1 step a head like for sakala s and then a then k and then l like this lets see the result

qs = "Ace snow"
print('ace' in qs)#false
print('snow' in qs)#true
print('ow' in qs)#true
print('Now' in qs)#false

saad = "pasang"
print(len(saad))
print(saad[1:4:2])

hap = "RUMPUM"
print(hap[1::3])