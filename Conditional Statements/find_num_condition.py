numbers = [12, -5, 8, 0, 15, 20, -3, 25]

for num in numbers:

    if num < 0:
        continue

    if num == 0:
        break

    if num % 5 == 0:
        print("Multiple of 5:", num)
