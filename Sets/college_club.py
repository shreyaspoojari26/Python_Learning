cricket = {"Rahul", "Aman", "Priya", "Kiran"}
football = {"Priya", "Sneha", "Aman", "Ravi"}

print("Students in both clubs:", cricket & football)
print("All club members:", cricket | football)
print("Only cricket:", cricket - football)
print("Only football:", football - cricket)
print("In exactly one club:", cricket ^ football)
