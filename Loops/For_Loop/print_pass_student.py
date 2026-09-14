students = {
    "Rahul": 65,
    "Kiran": 38,
    "Arun": 82,
    "Ravi": 29,
    "Shreyas": 75
}

for name, marks in students.items():

    if marks < 40:
        continue

    print(name, ":", marks)
