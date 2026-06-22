                                                # day 9 method to use the list

#in this lesson we will continue to learn about lists and some common methods associated with them like  append(), pop(), and sort()

#first append() , it is used to add item to the end of the list. for eg

a = ["pasang",90,121,1,1,2,3]
a.append("pop")
print(a)
#what we did just write the variable name and use .append and add what u want to add in () and print it. next example as well

pp = ["OPO","Redmi",121,1,2,133,3,23,2]
pp.append(1)
print(pp)
print("Redmi" in pp) # checking if there is pp in the list or not

#now if u wanted nested like adding one list inside the list we do
io = [1,2,3,4,4,2,]
io_io = [3,23,23,4,]

io.append(io_io)
print(io)

#easy write what to do just declare 2 variable with diff name add value and at last same variable.append and inside the next declared variable name
            #variable.io(variable 2)
#nxt example

poo = [1,1,1,1,1,11,1,"POOOP"]
poo_poo = [1,2,3,2323,2,2,22,3,"NOONE IS NOONE"]

poo.append(poo_poo)
print(poo)

poo1 = [1,1,1,1,1,11,1,"POOOP"]
poo1_poo = [1,2,3,2323,2,2,22,3,"NOONE IS NOONE"]

poo1.append(poo1_poo)
print(poo1)

                                #!!!!!!!!!! NOTE: Now we learned about append now we will learn about extend 
                                                # extend will add all the value as a one like 
                                                    #in append if we use append it will create list inside list nested
                                                #but in extend it won't create nested instead will add all value
#for eg 

lk = ["PASANGISGREAT","PASANGISGREAT2","PASANGISGREAT3"]
lk2 = ["Pasang",3,2,3,1,3,1]
lk.extend(lk2)
print(lk)

#next example 
kl = ['NO ONE IS GOD AMONG US', "KRATOS IS GOD OF WAR"]
kl_2 = ['LOLLLLL ','IT CANT BE TRUE']
kl.extend(kl_2)
print(kl)
#as we can see how we declare and how we execute the code and also how it is working it wont create any nested inside it.


                                                        #insert
#insert method() to insert element at a specific index in the list. this method accepts two argument.
#like insert helps to add elements in specific position 
#append : add at last , creates list
#extend() dosent,create list add everything just  a list of number
#insert () adding value in assigned position

#for eg for insert

bob = [1,2,3,4,5,6,7,9,10]
bob.insert(7,8)
print(bob)

#see so simple declaring the variable and after that inserting in the place i want to add like:
                    #bob.insert(7,8) this code says insert 8 after 7.....
                        # like 7 is from the list and adding 8 so the output is [1,2,3,4,5,6,7,8,9,10]
#next example
qq = [1,2,3,4,5,6,7,8,9]
qq.insert(3,3.5)
print(qq)
#simple i wanted to add 3.5 after 3 so i did qq.insert(3,3.5)

                                            #remove for remove removing the value from the list easy 
                                                #not the index
ww = [1,2,3,4,5,6,7,8]
ww.remove(3)
print(ww)
#remove one argument

                                            # now for the pop  
                                                #pop remove the index 
                                            
                                            #NOTE : WHAT IS THE DIFFERENCE BETWEEN INDEX AND VALUE????
                                                 # a= [10,20,30,40] , the value inside a 10,20,... they are called value
                                            #NOTE: INDEX ##
                                                # b = [10,20,30,40], index are where is it like read before 0 is 10, 1 is 20, 2is 30
#for eg

ee = [1,2,3,4,5,6,7,6]
ee.pop(2)
print(ee)
#3 is removed why ? because 2 is 3 from the variable ee

#now the thing is in index if we dont pop any indexes it will remove the value from the last

#for eg
rr = [1,2,34,56,7,8,8,9,9,99,9,121111111111111111111]
rr.pop()
print(rr)
#see it removed 12111111111111111111111 cause as told if no index are mentioned it will remove from the last

                                                        #clear() clear is used to clear all the value from the list
#for eg

tt = [12,3,4,13,1,3,2,4,23,1,2,1]   
tt.clear()
print(tt)
#see it cleared everything

                                                        #sort() sort is used to sort like put everything in order 
#for eg
yy = [1,3,2,6,5,4,7,8,0] #putting the number in random place
yy.sort() #this will help to put every number in order
print(yy)

                                                        #NOTE: sort() and sorted() and diff
                                                        #sort is use to put evrything in order 
                                                        #while sorted() helps to sort but also return the value like creating the new one
#for eg
uu = [1,9,8,7,6,5,3,24,56,7]
uu_uu = sorted(uu)
print(uu)
print(uu_uu)
#like in the sort() we just need to declare one variable but for the sorted() we need to declare 2 variables as shown in above example.
#nxt example for sorted()

ii = [1,3,2,4,6,5,7,9,8,0]
ii_ii = sorted(ii)
print(ii)
print(ii_ii)

#NOTE we need to print the both variable unlike other

                                                            #reverse()
                                                        #it is used to reverse the value
oo = [0,9,8,7,6,5,4,3,2,1]
oo.reverse()
print(oo)
#just reversing the value from the end to first easy


                                                            #index()
                                                            # it is used to see the first index if it is there or not
# for eg
pop_sicle = ["Oliver","Pasang","Passsss"]
pop_sicle.index("Oliver")
print(pop_sicle)
    #if the value is not found then it will print
    #traceback error



                                                        #NOTE: * `append()` → add one item
                                                        # * `extend()` → add multiple items
                                                        # * `index()` → find position
                                                        # * `sort()` → sort same list
                                                        # * `sorted()` → return new sorted list
                                                        # * `reverse()` → reverse list order
                                                        # * `clear()` → remove all items
                                                        # * `pop()` → remove item by index / if pop() empty remove one index from last
