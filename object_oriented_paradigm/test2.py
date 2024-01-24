import csv

class Person:
    
    all = []
    
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        
        Person.all.append(self)
        
    @classmethod
    def call_csv(cls):
        
        with open("sam.csv", "r") as open_csv:
            reader = csv.DictReader(open_csv)
            
            for data in reader:
                Person(data["Name"], data["Age"])
                
    def __repr__(self) -> str:
        return f"{self.name}, {self.age}"

        
        
    

Person.call_csv()

print(Person.all)

for i in Person.all:
    print(i.name)
        
    