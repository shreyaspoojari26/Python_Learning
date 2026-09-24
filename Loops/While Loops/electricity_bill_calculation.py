units = int(input("Enter units: "))

bill = 0

while units > 0:

    if units > 100:
        bill += 100 * 5
        units -= 100
    else:
        bill += units * 5
        units = 0

print("Bill:", bill)
