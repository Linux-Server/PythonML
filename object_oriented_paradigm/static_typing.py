class Person:
    def __init__(self,name:str, age:int, height:float, status:bool=False) -> None:
        
        assert type(status) == bool, "Pass an bool valus man"
        self.name= name
        self.age = age
        self.height= height
        self.status = status
        

person_one = Person("Sachin", 30, "scahin", True)
print(person_one.status)

# print(person_one.calculate_bmi())

