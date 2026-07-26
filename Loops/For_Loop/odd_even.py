numbers = [5, 12, 8, 20, 15]

even = []
odd = []

for item in numbers:
    if item % 2 == 0:
        even.append(item)
    else:
        odd.append(item)

print("even number", even)
print("odd number", odd)
