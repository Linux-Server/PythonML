import csv
class Person:
    
    all = []
    
    def __init__(self,name) -> None:
        self.name= name
        Person.all.append(name)
    def instance_method(self):
        print("Hello instance", self.name)
        
    @classmethod
    def class_method(cls):
        print("The class methos is active")
        with open('sam.csv', 'r') as f:
            reader = csv.DictReader(f)
            print(reader)
            
            for i in reader:
                print(i)
                Person(i["Name"])
        
        
        
        
        
person_one = Person("Sachin")

person_one.instance_method()

Person.class_method()

print(Person.all)
