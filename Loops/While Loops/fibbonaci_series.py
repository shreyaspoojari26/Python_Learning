n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a)
    
    next_num = a + b
    a = b
    b = next_num
    
    i += 1
