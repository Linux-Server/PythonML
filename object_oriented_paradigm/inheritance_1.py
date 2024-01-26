class Item:
    all = []
    def __init__(self,name, price) -> None:
        self.name = name
        self.price = price
        print("Item construct")
        Item.all.append(self)
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name},{self.price})"
        
        

class Phone(Item):
    
    all = []
    
    def __init__(self, name,price,broken = False) -> None:
        self.name =name
        self.price= price
        self.broken = broken
        print("Phone constructor")
        Phone.all.append(self)
        super().__init__(name,price)
        
class Laptop(Item):
    all = []

    
    def __init__(self, name,price,broken = False) -> None:
        self.name =name
        self.price= price
        self.broken = broken
        print("Laptop constructor")
        Laptop.all.append(self)
        super().__init__(name,price)
            
  
phone_one = Phone("Samsung", 100, False) 
phone_two = Phone("Nokia", 200, True) 
laptop_one = Laptop("MacAir", 999, False)  

print(Phone.all)  
print(Item.all)  
print(Laptop.all)  

