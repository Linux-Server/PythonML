import sys
import timeit

my_list = ["sam", True]
my_tup = ("sam", True)

print(sys.getsizeof(my_tup),"bytes")
print(sys.getsizeof(my_list),"bytes")

print(timeit.timeit(stmt="(1,2,3,4,5)", number=100000))
print(timeit.timeit(stmt="[1,2,3,4,5]", number=100000))