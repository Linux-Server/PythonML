# List
# how to declare empty list?
list_one = []
list_two = list()

# add

list_one.append(1)
print(list_one)

#add more
# list : mutable,growable,duplicate allow

list_three = [2,4,1,5,6,3]
list_three.remove(4)
print(list_three)
list_three = [2,4,1,5,6,3]
#  how to update a list by index ?
print(len(list_three))
print(list_three.count(6))

if 4 in list_three:
    print("four found")

# Slicing
list_three = [2,4,1,5,6,3]
print(list_three[3:1:-1])
# how to create a list = [5,5,5,5,5]
list_three = [5]*5
print(list_three)
list_three = [i * i for i in list_three]
print(list_three)

# copy
l1 = list([1,2,3])
print(l1)
l2 = list(l1)
print(l2)
l2.append(10)
print(l1,l2)

#sort
l1 = [1,3,5,7,2,4,6]
l2 = l1.sort()
print(l1)


#concat two list
l1 = [10,20,30]
l2 = [60,70,80]
print(l1.extend([1,2,3]))
print(l1)
