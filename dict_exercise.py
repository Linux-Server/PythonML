my_dict = {}
def add(num):
    
   
    if my_dict.get(num):
        print("The valu of the item is", my_dict.get(num))
        my_dict[num] += 1
        
        # my_dict[num] += 1
    else:
        print("The item doesnt found")
        
        my_dict[num] = 1
   
        


add(1)
add(2)


print("--------------------------")

print("The outcome {}".format(my_dict))



# {1:1 ,2:1}