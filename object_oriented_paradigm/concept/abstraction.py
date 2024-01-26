# Hiding unnecessary details from the user
# for example making a function private , which can be accesable inside class


class Person:
    def __connect(self):
        print("hello private function")

    def sam(self):
        self.__connect()


person = Person()
person.sam()