students = []

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added!")


def view_students():
    if len(students) == 0:
        print("No students available")
    else:
        for student in students:
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print()


while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Program ended")
        break

    else:
        print("Invalid choice")
