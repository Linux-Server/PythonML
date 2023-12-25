def divide(a,b):
    return a/b





try:
   print(divide(10,0))
   
except ZeroDivisionError as e:
    print("Zero div error")
    
except Exception as e:
    print("Something went wrong : ", e)

