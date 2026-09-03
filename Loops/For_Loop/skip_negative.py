#Skip Negative and Stop at Zero
for i in range(10):
    num = int(input("Enter number: "))

    if num < 0:
        continue
    if num == 0:
        break

    print("Number:", num)
