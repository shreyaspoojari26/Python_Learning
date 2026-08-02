s = {1, 2, 3, 4, 5, 2, 3} # duplicates auto removed

print("Set:", s) # {1, 2, 3, 4, 5}
print("Length:", len(s))
s.add(6)
s.remove(1) # error if not found
print("After add/remove:", s)
