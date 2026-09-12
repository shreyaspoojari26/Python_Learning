marks = [78, -1, 65, 90, 0, 55, 82]

for mark in marks:

    if mark < 0:
        continue

    if mark == 0:
        break

    if mark >= 75:
        print("Good:", mark)
