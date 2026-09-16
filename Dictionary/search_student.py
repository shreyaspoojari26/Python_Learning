students = {
    "Rahul": 65,
    "Kiran": 38,
    "Arun": 82,
    "Ravi": 55,
    "Shreyas": 75
}

search = input("Enter student name: ")

for name, marks in students.items():

    if name != search:
        continue

    print("Student found:", name)
    print("Marks:", marks)
    break
else:
    print("Student not found")
