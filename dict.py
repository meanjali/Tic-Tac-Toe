phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook["Jake"] = 938273443
del phonebook["Jill"]
print(phonebook)

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")



Dictionary1 = {'A': 'Geeks', 'B': 'For'} 
  
# Printing keys of dictionary, rreturn list of keys
print("Keys before Dictionary Updation:") 
keys = Dictionary1.keys() 
print(keys) 
  
# adding an element to the dictionary 
Dictionary1.update({'C':'Geeks'}) 
  
print('\nAfter dictionary is updated:') 
print(keys) 



# Python program to combine two dictionary 
# adding values for common keys 
from collections import Counter 
# initializing two dictionaries 
dict1 = {'a': 12, 'for': 25, 'c': 9} 
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300} 
# adding the values with common key 
Cdict = Counter(dict1) + Counter(dict2) 
print(Cdict) 


import itertools  
import collections   
# initializing two dictionaries 
dict1 = {'a': 12, 'for': 25, 'c': 9} 
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300} 
# using defaultdict 
Cdict = collections.defaultdict(int) 
# iterating key, val with chain() 
for key, val in itertools.chain(dict1.items(), dict2.items()): 
    Cdict[key] += val 
print(dict(Cdict)) 

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Dict.update({"Sarah":9})
print(Dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
del Dict ['Charlie']
print (Dict)


Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in Dict.keys():
    if key in Boys.keys():
        print (True)
    else:       
        print (False)

'''
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = Dict.keys()
Students.sort()
for S in Students:
      print(":".join((S,str(Dict[S]))))
'''
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = list(Dict.keys())
Students.sort()
for S in Students:
      print(":".join((S,str(Dict[S]))))


Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print ("Length : %d" % len (Dict))


# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  
# Creating a Dictionary  
# with Integer Keys 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
  
# Creating a Dictionary  
# with Mixed keys 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 
  
# Creating a Dictionary 
# with dict() method 
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
  
# Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 

# Creating a Dictionary  
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
  
# accessing a element using key 
print("Acessing a element using key:") 
print(Dict['name']) 
  
# accessing a element using key 
print("Acessing a element using key:") 
print(Dict[1]) 
  
# accessing a element using get() 
# method 
print("Acessing a element using get:") 
print(Dict.get(3)) 

