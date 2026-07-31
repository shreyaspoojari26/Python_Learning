days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

day = input("Enter day: ")

if day in days:
    print(f"{day} is a valid day")
else:
    print("Invalid day")
