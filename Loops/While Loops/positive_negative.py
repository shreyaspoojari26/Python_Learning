positive = 0
negative = 0
zero = 0

count = 1

while count <= 5:

    num = int(input("Enter number: "))

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

    count += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
