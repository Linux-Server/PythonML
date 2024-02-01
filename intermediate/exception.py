# Raise an exception
x = 10
if x <= 0 :
    raise Exception("NO way")

# capture exception

try:
    print("Hello buddy")
    5/0
except Exception as e:
    print("Unable to dod so", e)

