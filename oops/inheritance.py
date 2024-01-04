class Parent:
    def __init__(self, name,age) -> None:
        self.name=name
        self.age=age

class Chils(Parent):
    def __init__(self,name,age, address) -> None:
        super().__init__(name,age)
        self.address = address
        


chils = Chils("Samray", 44,"Paris")
print(chils.age)