list = [1,2,3,4,5]

def find_even(num):
    if num%2 == 0:
        return True
    else:
        return False
    

result = filter(find_even, list)
print(result)

for i in result:
    print(i)