def add_student(dict, roll, name):
    dict[roll] = name

students = {}
add_student(students, 1, "Rahul")
add_student(students, 2, "Aman")
print(students) # {1: 'Rahul', 2: 'Aman'}
