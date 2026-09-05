# 1. Creating tuple
my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple)

# 2. Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# 3. Slicing
print("Slicing [1:4]:", my_tuple[1:4])

# 4. Length, Max, Min, Sum
print("Length:", len(my_tuple))
print("Max:", max(my_tuple))
print("Min:", min(my_tuple))
print("Sum:", sum(my_tuple))

# 5. Checking element exists
if 30 in my_tuple:
    print("30 is present")

# 6. Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked:", a, b, c)

# 7. Nested tuple & counting
t2 = (1, 2, 2, 3, 2, 4)
print("Count of 2:", t2.count(2))
print("Index of 3:", t2.index(3))

# 8. Converting list to tuple
my_list = [1, 2, 3]
converted = tuple(my_list)
print("List to tuple:", converted)
