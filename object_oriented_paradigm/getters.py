class Persons:

    def __init__(self, name, age) -> None:
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,val):
        self.__name = val




person_one = Persons("Samuraiyy", 22)
person_one.name = "ray"
person_one.name = "base"

print(person_one.name)
