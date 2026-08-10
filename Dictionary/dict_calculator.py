menu = {"tea": 10, "coffee": 20, "samosa": 15}

order = input("What do you want: ")
qty = int(input("Quantity: "))

if order in menu:
    bill = menu[order] * qty
    print("Total:", bill)
else:
    print("Item not available")
