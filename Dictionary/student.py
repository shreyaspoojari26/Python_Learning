student = {
    "name": "Shreyas",
    "USN": "4AL23EC001",
    "branch": "ECE",
    "semester": 5,
    "cgpa": 7.8
}

print(student)

student["semester"] = 6
student["phone"] = "9876543210"

print("\nUpdated Details")
print(student)

print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
