numbers = []

for i in range(10):
    num = int(input("Enter the number: "))
    numbers.append(num)
    
for item in numbers:
    if item % 2 == 0:
     print(item)
     


even_count=0
for item in numbers:
    if item % 2 == 0:
        even_count += 1

print(even_count)
