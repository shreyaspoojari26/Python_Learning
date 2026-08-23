students = [
    {"name": "Shreyas", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Pallavi", "marks": 91},
    {"name": "Arun", "marks": 45},
    {"name": "Kiran", "marks": 58}
]

total = 0

for student in students:

    print("Name:", student["name"])
    print("Marks:", student["marks"])

    if student["marks"] >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")

    total += student["marks"]

average = total / len(students)

print("\nAverage marks:", average)
