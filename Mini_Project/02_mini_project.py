numbers = [12, 5, 18, 7, 30, 4, 21]

i = 0
even = []
odd = []

total = 0
largest = numbers[0]
smallest = numbers[0]

while i < len(numbers):

    num = numbers[i]

    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

    total += num

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    i += 1

print("Even:", even)
print("Odd:", odd)
print("Total:", total)
print("Largest:", largest)
print("Smallest:", smallest)
