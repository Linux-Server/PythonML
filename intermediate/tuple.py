# tuple is ordered, immutable, allow duplicate
# the only diffrence with list is, it cannot be changed after creation

my_tup = ("Max", True, 22)

for i in my_tup:
    print(i)

if "Max" in my_tup:
    print("yes")

my_tup = (1,2,3,4,2,2)
print(my_tup.count(2))
print(my_tup.index(3))

# convert a tuple ti list and vice-versa
my_tup = ("sam","ram","cram")
my_list = list(my_tup)
print(my_list)
my_tup = tuple(my_list)
print(my_tup)

# Slicing a tuple
slice_tup = my_tup[0:]
print(slice_tup)

# destructure or un-packing a tuple
test_tup = True, "Sam", 100
status,name,amount = test_tup
print(name)
print(test_tup)
i1,*i2 = test_tup
print(i1)
print(i2)

