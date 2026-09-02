#Student Dictionary 
student = {
    "name": "Shreyas",
    "age": 21,
    "marks": 75
}

print(student)

student.update({"marks": 85, "grade": "A"})

print(student.get("name"))
print(student.get("marks"))
print(student.keys())
print(student.values())
print(student.items())
