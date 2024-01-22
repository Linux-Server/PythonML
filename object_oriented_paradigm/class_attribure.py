class Person:
    nick_name = "Sachin"  #Class attribute
    pay_rate = 10 # 80 percent pay rate
    
    def __init__(self, name,age, nick) -> None:
        self.name = name
        self.age = age 
        self.nick_name = nick
        
    def calculate_pay_class_level():
        return 10 * Person.pay_rate
    
    def calculate_pay_instance_level(self):
        return 10 * self.pay_rate
        
        

person_one = Person("Anju", 29, "leslie")

print(person_one.nick_name)  #leslie
print(Person.nick_name) # Sachin


# Magic attribute - print all the class attibute

print(Person.__dict__["nick_name"])  

print(Person.__dict__)  # give all attribute at class level
print(person_one.__dict__) # give all attibute at instance level

# Accssing class attibute at instance level vs class level

print(" Class level" ,Person.calculate_pay_class_level())
person_one.pay_rate = 100
print(" Instance level ", person_one.calculate_pay_instance_level())

