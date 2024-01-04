class Parent:
    def __init__(self, name,age) -> None:
        self.name=name
        self.age=age

class Chils(Parent):
    def __init__(self,name,age, address) -> None:
        super().__init__(name,age)
        self.address = address
        


chils = Chils("Samray", 44,"Paris")
# print(chils.age)


class A:
    a=10
    
class B(A):
    a=20
    
class C(B):
   #a=30 
   pass
   
call_class = C()
print(call_class.a)
#Is sub class check
print(issubclass(B,A))

#Is instance check

print(isinstance(call_class,A))