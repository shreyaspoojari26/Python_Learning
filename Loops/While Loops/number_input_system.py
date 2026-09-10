""" NUMBER INPUT SYSTEM"""
numbers = []

while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break

    if num < 0:
        continue

    numbers.append(num)

print("Numbers:", numbers)
