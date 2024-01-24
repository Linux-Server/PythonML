import csv
import os

class Person:
    name = "Admin"
    age =1200
    status = True
    
    
    def __init__(self,name,age):
        assert age>25, "Age should be above 25"
        self.name= name
        self.age=age
        
    @classmethod   
    def import_csvs(cls):
        current_script_path = os.getcwd()
        print(current_script_path)
        with open(current_script_path + "/sam.csv", 'r') as data:
            print(data)

            reader = csv.DictReader(data)
            
            for i in reader:
                print(i)
            


person_three = Person("Sachin", 28)

print(Person.__dict__["name"]) 

Person.import_csvs()





