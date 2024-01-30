# Dict : key-value pair, un-ordered, mutable

my_dict = {"name": "Sachin", "age":28}
mydict = dict(name="Anju", age=28)

print(my_dict, mydict)

# add to dict
mydict["height"] = 180
mydict["height"] = 181

print(mydict)
# remove from dict
del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)
# removes that last item
my_dict.popitem()
print(my_dict)

try:
    print(my_dict["name"])
except:
    print("Not found")

# initialize a dict

dicts = {}
dicts["name"] = "Raymond"
dicts["since"] = 1918
for key in dicts.keys():
    print(key)

for value in dicts.values():
    print(value)

for key,value in dicts.items():
    print(key,value)

print("Original : ", dicts)
dicts_copy = dicts
print("Copy", dicts_copy)
dicts_copy["brand"] = "Clothes"
print(dicts)

# Above method ovewrite the changes the original as well the copy dicts
# Inorder to keep the original one intact
dict_tmp = dict(name="Samurai", age=22)
dict_tmp_cpy = dict(dict_tmp) # or use copy()
dict_tmp_cpy["skill"] = "assassin"
print(dict_tmp, dict_tmp_cpy)

# Merge two dicts
org = {"name":"Stephen", "age":64}
dup = dict(name="Brady", email ="brady@gmail.com")
org.update(dup)
print(org)