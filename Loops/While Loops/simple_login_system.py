""" SYMPLE LOGIN  SYSTEM"""
correct_password = "SHREYAS26"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful!")
        break

    attempts -= 1
    print("Wrong password")

if attempts == 0:
    print("Account locked")
