#List
# Any data type cab be stored in list
# its also allows indexing

list1 = [1,2,3,4]
list2 = ["A","B"]
list3 = [1,"a",True]

#nested list

list4 = [1,[1,2,3],6]

print(list1)
print(list1, sep=" ")
print(*list1)

# Adding data into list

a = [10,20,30,40]
a.insert(len(a), 50)  # this will add 50 to the that index
print("The a is" , a)
# append will add it to last
a.append(60)
print(a)
#can also add another list to this list
a.extend([1,2,3])
print(a)
a.pop()
print(a)
#delete a particular
b = [1,2,3,4,5]
b.pop() # [1,2,3,4]
b.pop(0)  #[2, 3, 4]
del b[0] #[3,4]
print(b)

c =[2,3,4,5]
c[0] = 100
print(c)