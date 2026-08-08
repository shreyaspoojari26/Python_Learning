def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    else:
        return "C"

print(grade(85)) # A
print(grade(45)) # C
