
with open("./file_handling/sam.txt", mode= "r") as file:
    data = file.readline()
    print(data)
    
    
with open("./file_handling/new.txt", mode = "w") as file:
    data = file.write("Hello Boss")
    print(data)
    
#write muliple lines

with open("./file_handling/new2.txt", mode = "a") as file:
    data = file.writelines(["Hello Boss", "\nhow are you\n"])
    print(data)