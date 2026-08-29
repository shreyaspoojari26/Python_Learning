numbers = [12, -5, 0, 8, -10, 0, 25, -3]

positive = []
negative = []
zero = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
