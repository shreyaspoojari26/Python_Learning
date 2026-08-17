numbers = [12, 7, 25, 8, 30, 15, 4, 21]

largest = numbers[0]
smallest = numbers[0]
total = 0

for item in numbers:

    if item > largest:
        largest = item

    if item < smallest:
        smallest = item

    total += item

print("Largest:", largest)
print("Smallest:", smallest)
print("Total:", total)
