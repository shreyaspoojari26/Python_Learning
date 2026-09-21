products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000
}

search = input("Enter product: ")

price = products.get(search)

if price is None:
    print("Product not found")
else:
    print("Product:", search)
    print("Price:", price)
