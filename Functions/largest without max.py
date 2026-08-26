def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


numbers = [12, 45, 7, 89, 23]

result = find_largest(numbers)

print("Largest number:", result)
