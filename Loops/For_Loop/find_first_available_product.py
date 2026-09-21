products = {
    "Laptop": 0,
    "Mouse": 5,
    "Keyboard": 0,
    "Monitor": 8
}

for product, stock in products.items():

    if stock == 0:
        continue

    print("First available:", product)
    print("Stock:", stock)
    break
