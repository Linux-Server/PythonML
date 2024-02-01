# lambda - is anonymous function

adds = lambda x,y: x+y

print(adds(10,10))

my_list = [[1,8],[2,4],[3,6]]

new_list = sorted(my_list, key=lambda x: x[1])
print(new_list)

my_list = [1,2,3,4,5]
new_list = map(lambda x: x+100, my_list)
print(list(new_list))

# list comprehension
news = [x+100 for x in my_list]
print(news)