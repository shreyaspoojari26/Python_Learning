numbers = [12, 7, 25, 8, 30, 15, 4, 21]

i = 0
even = 0
odd = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        even += 1
    else:
        odd += 1

    i += 1

print("Even:", even)
print("Odd:", odd)
