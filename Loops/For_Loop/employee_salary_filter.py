employees = {
    "Rahul": 18000,
    "Kiran": 25000,
    "Arun": 15000,
    "Ravi": 32000,
    "Shreyas": 28000
}

for name, salary in employees.items():

    if salary < 20000:
        continue

    if salary > 30000:
        print("High salary found:", name, salary)
        break

    print(name, salary)
