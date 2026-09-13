students = ["Rahul", "Kiran", "Arun", "Ravi", "Shreyas"]

search = input("Enter name: ")

for student in students:
    if student != search:
        continue

    print("Student found:", student)
    break
