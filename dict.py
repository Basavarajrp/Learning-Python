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


#Shallow copy in nested dict..    
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

