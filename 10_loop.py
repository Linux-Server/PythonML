num = [10,20,30,40,50]

# for loop
for i in num:
    print(i)
    
# Range in loop

for i in range(10):
    print("The range is", i)


# while loop


count = 0 

while count < len(num):
    print("Ok")
    count +=1
    
# Enumerate func to get thye inde in for loop

for index, val in enumerate(num):
    print(index,val)