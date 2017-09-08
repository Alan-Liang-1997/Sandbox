def main():
    load_file()




def load_file():
    wishlist = user_input()
    out_file = open("wishlist.txt", "w")
    while wishlist != "Q":
        wishlist = input("What would you like for Christmas: ")
        print(wishlist, file=out_file)
    out_file.close()


def user_input():
    menu = """
    Q - Complete Wishlist"""
    print(menu)
    return input(">>> ").upper()

main()