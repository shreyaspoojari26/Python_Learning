names = ["Rahul", "Kiran", "Arun", "Ravi", "Shreyas"]

search = input("Enter name: ")

for name in names:

    if name != search:
        continue

    print("Name found:", name)
    break
else:
    print("Name not found")
