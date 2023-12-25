def sum(a,b):
    return a+b

print(sum(1,1))


#ARGS
def sum(*args):
    val = 0
    for i in args:
        val += i
        
    return val

print(sum(1,2,3,4,5,5))

#KWARGS
def sum(**kwargs):
    sums = 0
    for i,val in kwargs.items():
        sums += val
    
    return sums

print(sum(coffe=20,tea=30))