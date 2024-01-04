class MyFirstClass():
    index = "Author Book"
    print("Who wrote this?")
    
    def hand_list(self, philospher, book):
        print(philospher + " wrote the book " + book)
    
    
mu_class = MyFirstClass()
print(mu_class.hand_list("Pluto", "Killer"))
        