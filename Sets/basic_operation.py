A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("A:", A)
print("B:", B)

print("Union | :", A | B)           # {1,2,3,4,5,6,7,8}
print("Intersection &:", A & B)     # {4, 5}
print("Difference A-B -:", A - B)   # {1, 2, 3}
print("Difference B-A -:", B - A)   # {6, 7, 8}
print("Symmetric Diff ^:", A ^ B)   # {1,2,3,6,7,8}
