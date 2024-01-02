


def reverse(str):
    print("data : {}".format(str))
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + "s"
    


data = reverse("cat") 
print(data)