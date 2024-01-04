class Recepi():
    def __init__(self,names,ages,nation) -> None:
       self.name = names
       self.age = ages
       self.nation = nation
       
    def contents(self):
        print("hi" + self.name)
        
    
       
       
first_person = Recepi("sachin", 28, ["killer", "clan"])
second_person = Recepi("Anju", 28, ["lover", "gem"])

print(first_person.nation)
print(first_person.contents())