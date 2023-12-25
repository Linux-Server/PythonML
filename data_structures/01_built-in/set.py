#Set
#set wont allow duplicate value
#can't take index
a = {1,2,3,4,5,5}
print(a)
#add an element
a.add(6)
print(a)

#remove an element use either remove or sicard
a.remove(5)
a.discard(6)
print(a)

#combine two sets by removing the duplicate values
b = {1,2,3,4,5,6}
print(a.union(b))
#another way for union
x ={1,2,3}
y={3,4,5}
print(x | y)
#Intersection
print(x.intersection(y))
#another way of intersection 
print(x&y)

#Set Diffrenece
print(x.difference(y)) # return all the elements x not in b
#another way
print(x-y)

#Symmetrical diffrence
print(x^y)
