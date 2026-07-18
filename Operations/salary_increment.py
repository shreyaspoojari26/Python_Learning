name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))

increment = salary * 0.10
new_salary = salary + increment

print(f"\nEmployee Name: {name}")
print(f"Old Salary: ₹{salary}")
print(f"Increment: ₹{increment}")
print(f"New Salary: ₹{new_salary}")
