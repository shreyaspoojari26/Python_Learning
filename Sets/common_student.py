python_students = {"Rahul", "Priya", "Aman", "Sneha"}
java_students = {"Aman", "Kiran", "Priya", "Meera"}

common = python_students & java_students
only_python = python_students - java_students
only_java = java_students - python_students

print("Both subjects:", common)
print("Only Python:", only_python)
print("Only Java:", only_java)
