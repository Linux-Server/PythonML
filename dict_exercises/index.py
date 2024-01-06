my_dict= {}

# Push data to dict (*it will accept multiple types)
my_dict[1] = 100
my_dict["status"] = True
# my_dict.clear()
# take the copy of a dict
my_dict_copy = my_dict.copy()

# create an empty dict and call calls fromkeys()
x = ("sam", "ram", "jam")
new_empty ={}.fromkeys(x, 0)

print(new_empty)
print(my_dict)

# get() method to check a value exist
first_value = my_dict_copy["status"]
print(first_value)

# items
x = my_dict.items()
print(x)
x = my_dict.keys()
print(x)
my_dict.pop(1)
print(my_dict)

my_dict.popitem()
print(my_dict)

my_dict = {1:"sam", 2:True}
my_dict.update({1:False})
print(my_dict)
my_dict.setdefault(100, "Smarya")
print(my_dict)








