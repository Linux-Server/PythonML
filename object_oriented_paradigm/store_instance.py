class Person:
    all = []
    def __init__(self, name , age) -> None:
        self.name =name
        self.age =age
        
        Person.all.append(self)
        
    def __repr__(self) -> str:
        return f"Item({self.name},{self.age})"
        


person_one =Person("Sachin",30)
person_two =Person("Anju", 29)
person_three = Person("Lesile", 31)




for i in Person.all:
    print("Name is :", i.name)
    
print(Person.all)
# How to represent above list in human readable way other than loop : use magic methof __epr__
