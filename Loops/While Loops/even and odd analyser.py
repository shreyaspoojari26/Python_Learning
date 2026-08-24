numbers = [12, 7, 25, 8, 30, 15, 4]

even = []
odd = []

i = 0

while i < len(numbers):

    if numbers[i] % 2 == 0:
        even.append(numbers[i])
    else:
        odd.append(numbers[i])

    i += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
