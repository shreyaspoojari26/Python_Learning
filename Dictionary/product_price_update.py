#Product Price Update 
product = {"name": "Laptop", "price": 50000, "stock": 10}

print(product)
product.update({"price": 48000, "stock": 15})

print(product.get("name"))
print(product.get("price"))
print(product.get("stock"))
print(product.keys())
print(product.items())
