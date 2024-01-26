class Person:
    def __init__(self,name):
        self.__name = name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,val):
        self.__name = val



person_one = Person("Sachin")

person_one.name ="leslie"

print(person_one.name)
