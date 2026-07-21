num = int(input("Enter the limit: "))

even = 0
odd = 0

for i in range(1, num + 1):

    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers =", even)
print("Odd numbers =", odd)
