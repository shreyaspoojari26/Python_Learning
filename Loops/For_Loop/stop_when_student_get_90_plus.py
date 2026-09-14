students = {
    "Rahul": 65,
    "Kiran": 72,
    "Arun": 91,
    "Ravi": 55,
    "Shreyas": 85
}

for name, marks in students.items():

    if marks < 40:
        continue

    if marks >= 90:
        print("High scorer found:", name)
        break

    print(name, ":", marks)
