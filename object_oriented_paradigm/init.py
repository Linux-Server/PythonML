# Constructor

#  Collection of method that start with __ (double underscore) is magic methods

class Item:
    def __init__(self, name="Samsung",price= 505,quantity =99) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        print("Im created")
        print(f"Im created one again: {name}")
    
    def calculate_price(self):
        return self.price * self.quantity




first_item = Item()
print(first_item.name)

# Additional states to object
first_item.status = False

print(first_item.status)
print(first_item.calculate_price())



