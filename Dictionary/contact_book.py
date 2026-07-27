contacts = {
    "Amma": "9876543210",
    "Friend": "9123456789",
    "Teacher": "9988776655"
}

name = input("Whose number do you want? ")
print(contacts.get(name, "Not found"))
