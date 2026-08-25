numbers = [10, 20, 30, 40, 50]

reverse = []

i = len(numbers) - 1

while i >= 0:

    reverse.append(numbers[i])

    i -= 1

print("Original:", numbers)
print("Reverse:", reverse)
