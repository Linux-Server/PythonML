def predict_outcome():
    computer_choice = "Rock"
    player_choice = "Paper"

    return player_choice



# List, Dict, Set , Tuple

outs = predict_outcome()
print("The output will be",  outs)


my_list = ["sam","ram","jam","jill","roy"]
my_list.append("alice")
print("My list : ",  my_list)
my_list.remove("alice")
my_list.pop(0)
new_list = my_list.copy()
print("My list : ",  my_list)
print("New list : ",  new_list)
my_list.extend(new_list)
print(my_list)

list_one = ["alice", "bob"]
list_two = ["stephen", "ray"]
list_one.extend(list_two)
print(list_two)

list_two.insert(0, "mary")
list_two.append("mary")
print(list_two)
my_count = list_two.count("mary")
print(my_count)
print(list_two)
list_two.sort()
print(list_two)
list_two.reverse()
print(list_two)
check = list_two.index("ray")
print(check)

# Dict
# we can store key value pair
my_dict = {}
print(type(my_dict))
my_dict[1] = "sam"
my_dict[2] = "ram"
my_dict[3] = "sam"
my_dict[3] = "alice"
print(my_dict)
print(my_dict.get(5))
my_dict.pop(3)
print(my_dict.values())
mytmp_list = my_dict.values()
new_dict = my_dict.copy()
print(new_dict)
my_dict.update({9 :"bob"})
print(my_dict)
my_dict.popitem()
my_dict.popitem()
print(my_dict.keys())
print(my_dict.items())
print(my_dict)

