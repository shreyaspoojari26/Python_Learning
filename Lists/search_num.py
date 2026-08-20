numbers = [10, 25, 7, 18, 30, 45]

target = 18
i = 0
found = False

while i < len(numbers):
    if numbers[i] == target:
        found = True
        break

    i += 1

if found:
    print("Number found")
else:
    print("Number not found")
