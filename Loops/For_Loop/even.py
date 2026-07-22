numbers = []

for i in range(10):
    num = int(input("Enter the number: "))
    numbers.append(num)
    
for item in numbers:
    if item % 2 == 0:
     print(item)
