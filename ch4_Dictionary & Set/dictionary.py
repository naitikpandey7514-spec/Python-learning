#dictionary
"""dictionary is a built in data type 
that store items in a form of keys and values pair """


dict = {
         "name":"naitik",     # this is way of writting dictionary
          "age":19,
          "branch":"AI|ML"
}


#dictionary method

dict = {
         "name":"naitik", 
          "age":19,
          "branch":"AI|ML"
}
print(dict.keys())      #gives all the keys of dictionary
print(dict.values())     #gives all the values of dictionary
print(dict.items())      #gives all the keys and values  of dictionary
print(dict.pop("age"))   #Removes and returns the value of a specified key
dict.update({'age': 25}) # its is use to add the items in dictinary or modified the dictionary
print(dict)
print(dict.clear())      # its clear the whole items from dictionnary