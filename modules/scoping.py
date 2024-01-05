def a():
    animal = "anju"
    
    def b():
        nonlocal animal
        animal = "sachin"
        # print("The b is "+ animal)
    
    
    # print("The first call", animal)
    b()
    print("The fit call", animal)

    

animal = "leslie"
a()
# print("the final", animal)