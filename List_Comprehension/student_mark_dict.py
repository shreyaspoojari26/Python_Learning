students = {
    "Rahul": 65,
    "Kiran": 38,
    "Arun": 82,
    "Ravi": 45
}

passed = {name: marks for name, marks in students.items() if marks >= 40}

print(passed)
