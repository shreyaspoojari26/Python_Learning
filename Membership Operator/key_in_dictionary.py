marks = {"Rahul": 85, "Priya": 92, "Aman": 78}

name = input("Enter student name: ")

if name in marks:
    print(f"{name}'s marks = {marks[name]}")
else:
    print("Student not found")
