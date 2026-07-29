marks = {}

n = int(input("How many students? "))

for i in range(n):
    name = input("Enter name: ")
    score = int(input("Enter marks: "))
    marks[name] = score

print("\nStudent Marks:", marks)

# Find highest scorer
topper = max(marks, key=marks.get)
print("Topper:", topper, "with", marks[topper], "marks")
