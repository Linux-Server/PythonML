#Dict and Set have same parentesis
#empty bracket type will be be a dict
a = {1:"sam", 2:"ray"}
print(type(a))
print(a)
a[1] = "sachin"
print(a)
del a[1]
print(a)

#add new item to dict
a[1] ="sam"
print(a)
#update value
a[1]=10
print(a)

for i,val in a.items():
    print(i, val)

