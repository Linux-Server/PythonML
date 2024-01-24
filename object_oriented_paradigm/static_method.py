class Person:
    
    @staticmethod
    def test_call(num):
        # Static method are not instance of class object and treat as a formal function with nor self
        if isinstance(num, int):
            print("Its a bool vals")
            return True
            
            


print(Person.test_call(20))