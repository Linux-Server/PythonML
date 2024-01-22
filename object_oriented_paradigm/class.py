class Item:
    def calculate_price(self,price,qty):
       return self.price* self.quantity


first_item = Item()

first_item.name = "Iphone"
first_item.price = 300
first_item.status = False
first_item.quantity = 10


print(type(first_item))

total_price = first_item.calculate_price(100,100)
print("Total price : ", total_price)