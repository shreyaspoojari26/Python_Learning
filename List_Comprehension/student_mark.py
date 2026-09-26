students = ["Chandan", "Darshan", "Narendra"]
marks = [25, 90, 78]

student_marks = {}

for i in range(1, len(students)):
    student_marks[students[i]] = marks[i]

print(student_marks)
