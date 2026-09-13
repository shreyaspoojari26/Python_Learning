numbers = [7, 13, 19, 25, 32, 40, 51]

for num in numbers:

    if num % 2 != 0:
        continue

    print("First even number:", num)
    break
