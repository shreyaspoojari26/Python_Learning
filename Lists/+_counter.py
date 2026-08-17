numbers = [12, 7, 25, 8, 30, 15, 4, 21]

even = []
odd = []

even_count = 0
odd_count = 0

for item in numbers:
    if item % 2 == 0:
        even.append(item)
        even_count += 1
    else:
        odd.append(item)
        odd_count += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Number of even values:", even_count)
print("Number of odd values:", odd_count)
