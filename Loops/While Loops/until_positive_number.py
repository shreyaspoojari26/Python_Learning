#Keep asking until a positive number is entered
num = int(input("Enter a positive number: "))

while num <= 0:
    print("Invalid number")
    num = int(input("Try again: "))

print("Accepted:", num)
