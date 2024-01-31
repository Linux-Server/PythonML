# string - ordered, immutable, text representation
my_str = "Hello World"
my_str_one = 'Hello str'
my_str_two  = "I'm Sachin"
my_str_three = 'I\'m Sachin'

# multiline string
my_str = """Hello Buddy
How are u!
Yor are looking good"""

print(my_str)

# remove whitespace
my_str = "Hell Yeah"
# strip won't change the original string , instead return to new variable
print(my_str.strip())
print(my_str.upper())
print(my_str.lower())
print(my_str.startswith("Hell"))
print(my_str.endswith("ah"))

# find index of a char
print(my_str.find('e'))
print(my_str.count('e'))
print(my_str.replace("Yeah", "No"))

# convert string into list

my_str ="hello how are you my boy"
my_list = my_str.split(" ")
print(my_list)
# convert back to string

my_strs = " ".join(my_list)
print(my_strs)

# Create a list contain "s" five times
my_list = ['s'] * 5
print(my_list)

# convert above list into string
my_str = "".join(my_list)
print(my_str)

# convert that back to list
lists= my_str.split(" ")
print(lists)

# formatting string
my_name = 10.928388
my_var = f"hello {my_name}"
print(my_var)
