
# list comprehension
data =[1,2,3,4,5,6]
newlist = [i+1 for i in data if i>3]
print(newlist)

# Dict comprehension
usedict = {1:100, 2:200, 3:300}
usedict = {i:i for i in range(10)}
print(usedict)