# Mechanism of restricting the direct access of some attribute of program
class Person:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        assert len(new_name) > 10
        self.__name = new_name
        return  self.__name



person_one = Person("Sachin")
print(person_one.name)
person_one.name = "Killerjdjqwfe"
print(person_one.name)
