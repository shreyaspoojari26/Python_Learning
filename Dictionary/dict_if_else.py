user = input("Enter username: ")

users = {"admin": "1234", "guest": "guest"}

if user in users:
    print("User found")
else:
    print("User not found")
