#SIMPLE MENU
while True:
    print("\n1. Add Number")
    print("2. View Numbers")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        num = int(input("Enter number: "))
        print("Number added:", num)

    elif choice == "2":
        print("Viewing numbers...")

    elif choice == "3":
        print("Program ended")
        break

    else:
        print("Invalid choice")
