#Search The Elements 
t = (10, 20, 30, 40)
n = int(input("Enter element to search: "))
if n in t:
    print(f"{n} found at index {t.index(n)}")
else:
    print("Not found")
