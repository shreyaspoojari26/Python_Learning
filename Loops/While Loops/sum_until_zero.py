""" SUM UNTIL ZERO ENTERS"""
total = 0

while True:
    num = int(input("Enter number: "))

    if num == 0:
        break

    total += num

print("Total:", total)
