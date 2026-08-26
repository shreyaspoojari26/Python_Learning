def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 85:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 35:
        grade = "D"
    else:
        grade = "Fail"

    return total, average, grade


# Taking input
marks = []

for i in range(5):
    mark = int(input(f"Enter mark {i + 1}: "))
    marks.append(mark)

# Calling the function
total, average, grade = calculate_result(marks)

print("\n--- Result ---")
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
