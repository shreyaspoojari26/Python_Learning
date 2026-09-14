students = {
    "Rahul": 65,
    "Kiran": 38,
    "Arun": 82,
    "Shreyas": 75
}

search = input("Enter student name: ")

for name, marks in students.items():

    if name != search:
        continue

    print("Student:", name)
    print("Marks:", marks)
    break
