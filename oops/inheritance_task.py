class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c

   def alpha(self):
       c = self.c + 1
       return c

a = A(1)
print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

   print(a.alpha())
   d = 5
   print(d)
   print(a.alpha())

print("Instantiating B..")
b = B(a)
print(a)