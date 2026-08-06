age = int(input("Enter age: "))
is_student = input("Are you student? y/n: ")

if age < 12 or is_student == 'y':
    print("50% Discount")
else:
    print("No Discount")
