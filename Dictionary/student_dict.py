# 1. Create a dictionary
student = {
    "name": "Rahul",
    "age": 16,
    "grade": "10th"
}

# 2. Print the student's name
print("Name:", student["name"])

# 3. Update the grade
student["grade"] = "11th"

# 4. Add a new key
student["school"] = "Sunrise High School"

# 5. Loop through and print all key-value pairs
for key in student:
    print(key, ":", student[key])
