#Mobile Details
mobile = {"brand": "Samsung", "price": 25000}

mobile.update({"price": 22000, "storage": "128GB"})

print(mobile)
print(mobile.get("brand"))
print(mobile.get("price"))
print(mobile.get("storage"))
print(mobile.keys())
print(mobile.items())
