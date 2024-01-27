# List :  ordered,mutable and allows duplicate elements - like an array
# it can accommodate multiple data types
list_one = [1, 2, 3, "sam", False, "sam"]
print(list_one)

# How to create an empty list

list_two = []
print("Empty list : ", list_two)

# How access from a list
# we will get index error, if we go out of bounds
first_item = list_one[0]
last_item = list_one[-1]
print("first item : ", first_item)
print("last item : ", last_item)

# how to iterate over a list

for i in list_one:
    print("loop :", i)

# to check whether a item inside a list

if "sam" in list_one:
    print("Yes")

# check the len of list
print(len(list_one))

# append/add item to list
list_one.append("ray")
print(list_one)

#insert item at a specific position
list_one.insert(1,"blue")
print(list_one)

# pop/remove item from last
list_one.pop()
print(list_one)

# remove item from a specific index
list_one.remove("sam")
print(list_one)

# reverse a list
list_one.reverse()
print(list_one)



# remove all elem from a list
list_one.clear()

# sort a list - it will only work if for int and str
list_three = [15, 3, 7, 2, 7]
list_three.sort()
print(list_three)

# keep the original list create a new sorted one
original = [2,4,1,5,2,7]
sorted = sorted(original)
print(sorted)

# create a new list with same item multiple times
new_list = ["sam"] * 5
print(new_list)

# concat two list

new_list =  [10,2,3,4,5]
new_list_one = [1,2,3,4,5]
new_list = new_list + new_list_one
print(new_list)

# selecting array with index range - Slicing
new_list = [1, 2, 3, 4, 5]
a = new_list[1:5]  # [:5] or [1:]
print(a)
new_list = [1,2,3,4,5,6,7,8,9]
two_step = new_list[::-1] # reverse a list
print(two_step)

# copy a list to another

list_org = ["apple", "orange", "pineapple"]
copy_list = list_org  # this will point two list to sam memory location
# when updating one list can cause update on another one
# the proper method of copy is using copy function or slicing or list()
list_tmp = list_org.copy()
list_tmp_one = list(list_org)
list_tmp_two = list_org[:]

# Advanced method of creating a new list
new_list =[1,2,3,4,5,6]
advan_list = [i*i for i in new_list]
print(advan_list)


