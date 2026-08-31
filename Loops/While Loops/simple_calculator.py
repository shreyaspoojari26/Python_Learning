while True:

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == "3":
        print("Calculator closed")
        break

    else:
        print("Invalid choice")
