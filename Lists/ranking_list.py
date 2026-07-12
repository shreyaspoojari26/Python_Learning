students = ["Shreyas", "Rahul", "Aman", "Ravi", "Kiran"]
marks = [85, 67, 92, 74, 88]

print("Students:", students)
print("Marks:", marks)

print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", sum(marks) / len(marks))

highest = marks.index(max(marks))
lowest = marks.index(min(marks))

print("Topper:", students[highest])
print("Lowest Scorer:", students[lowest])
