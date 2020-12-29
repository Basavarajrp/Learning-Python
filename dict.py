#-------------------Declaring the dict in python and accessing the values using key:------
phonebook={
    "Basu":2424,
    "Pinki":2244,
    "Punter":4422
}
print(phonebook["Pinki"])
print()







#------------------Creating the dict with comprehesion way:--------------------------------
squares = {i:i*i for i in range(10)}
print(squares)
print()








#--------------------Iterating or Traversing the dictonaries:------------------------------
students={"Name":"Basu","Age":23,"Height":5.8,"Weight":62}

#method1:Traversing the key..
for key in students:
    print(key)
print()   

#method2:Traversing the values..
for key in students:
    print(students[key])
print()    

#------OR-----------
for values in students.values():
    print(values)
print()    

#method3:Traversing the key and values both at a time..
for key,value in students.items():  
    print(key,' ',value)












#------------------------Coopy and Deep coopy----------------------------------------
"""If changes made in one dictonarie and other does not get effected
then it is called deep coopy..
If changes made in one and if other get effect then it is shallow copy.."""
#shallow copy..
a = {1:99,2:24,3:45,4:7}
b=a
print("a before changes:",a)  #before changing..
print("b before changes:",b)
b[1]=1
print("a after changes:",a)  #after changes made to a b also gets effected these is shallow copy..
print("b after changes:",b)

#deep copy
c = a.copy()
c[1]=4
print(a)     #Here changes made to c, a will not get effected these is deep copy..
print(c)
print()

#Shallow copy and deep copy in nested dict..    
std = {
    'Name':"Basu",
    'Age':23,
    'Phno':{
        "mobile":9090,
        "Land":8080,
    },
    'Place':{
        "Res":"Bangalore",
        "Perm":"Hydrabad",
    },
}
#shallow copy
a = std.copy()
a['Phno']['Land']= 2424
print(a)    #changes made to a, but std also got effected this is shallow copy..
print(std)
print()
#deep copy
"""whenever there are nested dict the same references get copied 
changes made to one will effect other therefore we make use of copy module.."""
import copy
b=copy.deepcopy(std)
b["Place"]["Perm"]="Mysore"
print(std)  #changes made to b, will not effect the std this is deep copy 
print(b)    #make use of copy module whenever there is nested dict,list,tuples..
print()










#----------------------Collections module in python----------------------------------
print("collections.OrderedDict: Remember the Insertion Order of Keys...")
import collections
d = collections.OrderedDict(one=1,two=2,three=3)
print(d)

d['four']=4   #inserting new elements..
print(d)

print(d.keys())
print(d.values())
print()
print('------------------------------------------------------------------------------------')
print("colections.defaultdict:Return Default Values for Missing Keys..")
print("Example 1")
from collections import defaultdict
dd = defaultdict(list)

dd['dogs'].append("Rufus")
dd['dogs'].append("Kathrin")
dd['cat'].append("Black_Cat")
dd['cat'].append("White_Cat")
print(dd)  #creats key and values of type-list..
print("Dogs :",dd['dogs'])

print("Creating the counter by normal method and also by defaultdict method...")
dic_counter = {}
lis = [1,2,3,4,5,4,3,6,6,7,8,9,4]
for i in range(len(lis)):
    if lis[i] not in dic_counter:
        dic_counter[lis[i]] = 1
    else:
        dic_counter[lis[i]] += 1
        
print("Total number of elements repeated :",dic_counter)  
print()
print("---------------------------------")
print("using defaultdict method..")
print("Example 2:")
food_list = 'spam spam spam spam spam spam eggs spam'.split()
food_count = defaultdict(int)  # default value of int is 0
for food in food_list:
    food_count[food] += 1  # increment element's value by 1     
print("---------------------------------")
print("Example 3:")
food_list = 'spam spam spam spam spam spam eggs spam'.split()
food_count = defaultdict(int)  # default value of int is 0
for food in food_list:
    food_count[food] += 1  # increment element's value by 1
    #0r
print(food_count)
for i,j in food_count.items():
    print(i," ",j)
print("-----------------------------------")
print("Example 4:")
city_list = [('TX', 'Austin'), ('TX', 'Houston'), ('NY', 'Albany'),
             ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'),
             ('TX', 'Dallas'), ('CA', 'Sacramento'), ('CA', 'Palo Alto'),
             ('GA', 'Atlanta')]
cities_by_state = defaultdict(list)
for state, city in city_list:
    cities_by_state[state].append(city)
    #OR
for state, cities in cities_by_state.items():
    print(state, ', '.join(cities))        
print()

print("------------------------------------")
print("Example 5:")

from collections import defaultdict

food_list = [
    "bread", "burger", "bread", "sandwich", "burger", "sandwich", "burger","donuts"
]

food_counter = defaultdict(int)
#default value of the int is zero

for i in food_list:
    food_counter[i] += 1  #increment food value by one...

print(food_counter)

#------OR---------------
print()

for i, j in food_counter.items():
    print(i, j)
print()  
print()
print("------------------------------------------------------------------------")
print("collections.ChainMap-Search Multiple Dictionaries as a Single Mapping")
from collections import ChainMap
dict1={"one":1,"two":2}
dict2={"three":3,"four":4}
chain = ChainMap(dict1,dict2)
print(chain) 
print(chain['three'])
print(chain['one'])
#print(chain['missing'])  gives key error - KeyError:'missing'
print()
print()

print("----------------------------------------------------------------------------")
print("types.MappingProxyType - A Wrapper for Making Read-Only Dictionaries..")
from types import MappingProxyType
writable  = {"one":1,"two":2} #this can be used to read as well as write..
read_only = MappingProxyType(writable) #this can be used to readonly..
print(read_only['one'])
print()
#read_only['one'] = 23 #Gives type error..

writable['one'] = 42 #will not give errox cause it is available for both reading and writting also...
print(read_only)
print('__________________________________________________________________________________________')