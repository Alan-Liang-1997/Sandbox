"""
Alan Liang
"""
name = input("Enter your name:")
while name == "":
    print("Enter a valid name")
    name = input("Enter your name:")
print(name[1:len(name):2])