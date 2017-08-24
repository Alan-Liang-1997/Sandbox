# def main():
#     wishlist = []
#     ammount = []
#     wishlist_count = 0
#     choice = 10
#     while choice != 0:
#         choice = (int(input("How many nice things have you said to people today?:")))
#         if choice > 10:
#             present = input("What would you like for Christmas?:")
#             entry = False
#             while entry is False:
#                 try:
#                     number_of_items = int(input("How many would you like?: "))
#                     if 0 < number_of_items <= 10:
#                         entry = True
#                     else:
#                         print("Number must be between 0 and 10")
#                 except ValueError:
#                     print("Invalid input; enter a valid number")
#             wishlist_count += 1
#             wishlist.append(present)
#             ammount.append(number_of_items)
#     print("Here is your wishlist:")
#     for i in range (0,wishlist_count,1):
#         print("{} x {}".format(ammount[i], wishlist[i]))
# main()
#
from operator import itemgetter
def main():
    wishlist = [["item a", 10], ["items b", 2]]
    wishlist.sort(key=itemgetter(1))
    print(wishlist)
main()