name = input("Enter Account Holder Name: ")
balance = int(input("Enter Current Balance: "))

print("\n1. Deposit")
print("2. Withdraw")

choice = int(input("Enter Your Choice: "))

if choice == 1:
    amount = int(input("Enter Deposit Amount: "))
    balance = balance + amount
    print("Deposit Successful")
    print("Updated Balance:", balance)

elif choice == 2:
    amount = int(input("Enter Withdrawal Amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Updated Balance:", balance)

    else:
        print("Insufficient Balance")

else:
    print("Invalid Choice")
