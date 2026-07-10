#set
''' set is a built in unordered mutable data type
 that store only unique collection of elements 
 '''

mum ={"hey",1,3,6,7,"set","of","words"} #the way of writing set

#methods of set

n1 = {1,5,3,7,3,8,}
n2 = {5,7,3,2,9,6}
print(n1.union(n2))        #give all the values of both the set without repeating
print(n1.intersection(n2)) #give all the common values of both the set
print(n1.difference(n2))   # give the value which are present in first set but not in second
print(n1.add("12"))        #add one element to the set
print(n2.update(["hello"])) #add multiples element to the set
print(n1.remove(5))         #Removes the specified element. If the element is not found, it gives an error.
print(n1.discard(12))      #Removes the element if it exists. If it doesn't exist, no error occurs.
print(n2.pop())            #Removes and returns a random element.
print(n1.clear())          #Removes all elements from the set.


