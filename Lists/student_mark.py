marks = []

mark = int(input("Enter mark 1: "))
marks.append(mark)

mark = int(input("Enter mark 2: "))
marks.append(mark)

mark = int(input("Enter mark 3: "))
marks.append(mark)

mark = int(input("Enter mark 4: "))
marks.append(mark)

mark = int(input("Enter mark 5: "))
marks.append(mark)

print("Marks:", marks)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Total Marks:", sum(marks))
print("Number of Subjects:", len(marks))
print("Average Marks:", sum(marks) / len(marks))
