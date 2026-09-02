employee = {"name": "Rahul", "salary": 25000}

print(employee)
employee.update({"salary": 30000, "bonus": 5000})

print(employee.get("name"))
print(employee.get("salary"))
print(employee.get("bonus"))
print(employee.keys())
print(employee.values())
