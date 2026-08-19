count = 0
even = 0
odd = 0
total = 0

largest = None
smallest = None

while count < 5:

    num = int(input("Enter a number: "))

    total += num

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

    count += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Largest:", largest)
print("Smallest:", smallest)
print("Total:", total)
