list1 = [10, 20, 30, 40]
list2 = [20, 40, 50, 60]

common = []

for number in list1:

    if number in list2:
        common.append(number)

print("Common elements:", common)
