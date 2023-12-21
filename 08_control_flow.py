bill_total = 1000

if bill_total>100 and bill_total<200:
    print("Its greater than 100")
    bill_total -=11 
elif bill_total> 200:
    print("Its greater than 200")
else:
    print("Lees than 100")
    
print("The bill total is :" + str(bill_total))


current = False

if not(current):
    print("On")
else:
    print("Off")