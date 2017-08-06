total = 0
quantity = int(input("Number of items: "))

while quantity <= 0:
    print("Invalid quantity")
    quantity = int(input("Number of items: "))

for i in range(0, quantity, 1):
    price = float(input("Price of item {}: ".format(i+1)))
    # While loop will ensure that a negative price is not accepted and re-prompt the user to enter a valid price
    while price < 0:
        print("Invalid price")
        price = float(input("Price of item: "))
    total = total + price
if total >= 100:
    total = total * 0.9
    total = float(round(total,2))
print('Total price for', quantity, 'items is $', total)