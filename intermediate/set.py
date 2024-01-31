# unordered, mutable and no duplicate
my_set = set()
print(type(my_set))
my_set.add(10)
my_set.add(10)
print(my_set)

# convert a list into set
my_set = set([1,2,3,4,2])
print(my_set)
my_set = set("Hello")
print(my_set)

# union
set_one = {1,3,5,7,9}
set_two = {2,4,6,8,9}
union_set = set_one.union(set_two)
intersect = set_one.intersection(set_two)
difference = set_one.difference(set_two)
print(union_set)
print(intersect)
print(difference)

set1 = {1,2,3,4}
set2 = {4,5,6,7,8}
set1.intersection_update(set2)
print(set1)
# Frozen set - immuatble set

my_set = frozenset([1,2,3])
print(my_set)



