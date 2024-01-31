import sys
import timeit
# Built-in data structures
#  List, tuple, Dict Set

# Dict vs Set
# Dict -key val pair, duplicate, ordered
# Set - un-order,no duplicates

my_dict = {}
my_set = set()
print(type(my_dict))
print(type(my_set))

# add to dict
my_dict["name"] = "Sam"
my_dict["age"] = 22

# del my_dict["name"]
# my_dict.pop("name")
print(my_dict)

if "age" in my_dict:
    print("true")

for key,value in my_dict.items():
    print(key, value)

tmp_dict = {"name": "Raymond", "since": 1978}
tmp_dict_one = dict(name= "Louuse", since= 1888)
print(tmp_dict_one)

# we can make a tuple as key but not a list
my_tup = (1,2,3)
my_dict = {my_tup: "Samray"}
print(my_dict)

my_dict = {"name": "Raymond", "since": 1978, "status":True}
my_dict_one =  dict(name= "Louuse", since= 1888)
my_dict.update(my_dict_one)
print("Out", my_dict)
new_dict ={i: i+100  for i in range(1,5)}
print(new_dict)
new_dict[4] = "Sam"
del new_dict[4]
new_dict.clear()
print(new_dict)

# Set
my_set = set([100,200])
my_set.add(300)
my_set.add(300)
my_set.remove(100)
print(my_set)
# my_set.update(400)
# print(my_set.union([1,2,3]).update(300))

my_tup =()
my_list = []
print(type(my_tup))
print(sys.getsizeof(my_tup))
print(sys.getsizeof(my_list))

print(timeit.timeit(stmt="()", number=100000))
print(timeit.timeit(stmt="[]", number=100000))




