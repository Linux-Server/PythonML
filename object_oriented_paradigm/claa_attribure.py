class Person:
    nick_name = "Sachin"  #Class attribute
    
    def __init__(self, name,age, nick) -> None:
        self.name = name
        self.age = age 
        self.nick_name = nick
        
        

person_one = Person("Anju", 29, "leslie")

print(person_one.nick_name)  #leslie
print(Person.nick_name) # Sachin