num = [2, 25, 26, 558, 856, 56, 45, 5, 45]

for i in num:
    if i == 856:
        break

    if i % 2 == 0:
        continue

    print(i)
