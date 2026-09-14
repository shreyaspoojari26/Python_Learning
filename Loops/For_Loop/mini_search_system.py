products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000
}

search = input("Enter product: ")

for product, price in products.items():

    if product != search:
        continue

    print("Product:", product)
    print("Price:", price)
    break
else:
    print("Product not found")
