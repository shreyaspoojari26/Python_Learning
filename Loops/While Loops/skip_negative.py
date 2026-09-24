while True:
    num = int(input("Enter number: "))

    if num < 0:
        continue

    if num == 0:
        break

    print("Positive:", num)
