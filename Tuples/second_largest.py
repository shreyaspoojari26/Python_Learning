nums = (12, 45, 7, 89, 23, 89)

unique = tuple(set(nums)) # remove duplicates
sorted_tup = tuple(sorted(unique))

print("2nd Largest:", sorted_tup[-2]) # 45
