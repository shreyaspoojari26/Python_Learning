students = {
    "Rahul": 35,
    "Kiran": 78,
    "Arun": 45,
    "Ravi": 28,
    "Shreyas": 82
}

for name, marks in students.items():

    if marks < 35:
        continue

    if marks >= 80:
        print("Excellent:", name, marks)
        break

    print("Passed:", name, marks)
