password = input("Enter Password: ")

print("Length:", len(password))
print("Has Minimum 8 Characters:", len(password) >= 8)
print("Has Uppercase:", password != password.lower())
print("Has Lowercase:", password != password.upper())
