marks = [65, 82, 45, 90, 73]

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print("Total:", total)
print("Average:", average)

if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
