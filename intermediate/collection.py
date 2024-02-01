from collections import Counter
from collections import namedtuple

# Counter
my_str = "aaaaaabbbbccccnnnnnnnnnnnn"
my_count = Counter(my_str)
print(my_count) # create a dict
print(my_count.keys())
print(my_count.values())
print(my_count.items())
print("most common :",my_count.most_common(1))
print("most common :",my_count.most_common(1)[0][0])
print(list(my_count.elements()))

# namedtuple
# this will create a class named Point
Point = namedtuple("Point", "x,y")
new_class = Point(10,20)
print(new_class.x)
