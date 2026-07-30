cart1 = {"milk", "bread", "eggs", "butter"}
cart2 = {"bread", "cheese", "eggs", "juice"}

print("Items in both carts:", cart1 & cart2)
print("Items only in cart1:", cart1 - cart2)
print("Items only in cart2:", cart2 - cart1)
print("All different items:", cart1 ^ cart2)  # symmetric difference
