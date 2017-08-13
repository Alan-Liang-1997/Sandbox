"""
Alan Liang
"""
def main():
    name = get_name()
    print(name[1:len(name):2])

def get_name():
    name = input("Enter your name:")
    while name == "":
        print("Enter a valid name")
        name = input("Enter your name:")
    return name

main()