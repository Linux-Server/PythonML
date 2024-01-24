class Father:
    
    
    def __init__(self, name="Murali") -> None:
        self.name = name
        
    
    def singing(self):
        print("Parent can sing")
        

class Mother:
    def __init__(self, name = "Sindhu") -> None:
        self.name = name
        
    def running(self):
        print("Mother can run")
    
    
class Child(Father, Mother):
    
    def __init__(self, name="Murali", child_name="sachin") -> None:
        super().__init__(name)
       # self.name = child_name
        
    def dancing(self):
        print("child can dance")
        
        

person = Child()
print(person.name)
person.running()