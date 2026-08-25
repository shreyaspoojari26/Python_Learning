cart = []

while True:

    print("\n1. Add item")
    print("2. View cart")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        item = input("Enter item: ")
        cart.append(item)

        print("Item added")

    elif choice == "2":

        if len(cart) == 0:
            print("Cart is empty")

        else:
            print("Cart:", cart)

    elif choice == "3":

        print("Thank you!")
        break

    else:
        print("Invalid choice")
