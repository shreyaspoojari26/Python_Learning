a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

if a+b>c and b+c>a and a+c>b:
    if a==b==c:
        print("Equilateral Triangle")
    elif a==b or b==c or a==c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")
