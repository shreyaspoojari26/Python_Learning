t = (1, 2, 3, 4, 5, 6, 76, 98)
even = 0
odd = 0
for i in t:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)
