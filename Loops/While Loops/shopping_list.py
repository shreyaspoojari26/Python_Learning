items = []

while True:

    print("\n1. Add item")
    print("2. View items")
    print("3. Remove item")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        item = input("Enter item: ")
        items.append(item)
        print("Item added")

    elif choice == "2":

        if len(items) == 0:
            print("List is empty")
        else:
            for item in items:
                print(item)

    elif choice == "3":

        item = input("Enter item to remove: ")

        if item in items:
            items.remove(item)
            print("Item removed")
        else:
            print("Item not found")

    elif choice == "4":

        print("Program ended")
        break

    else:
        print("Invalid choice")
