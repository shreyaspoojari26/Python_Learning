students = {
    "Rahul": 25,
    "Kiran": 32,
    "Arun": 35,
    "Ravi": 42,
    "Shreyas": 78
}

for name, marks in students.items():
    if marks < 40:
        continue

    print("First passing student:", name)
    print("Marks:", marks)
    break
