expense = int(input("Enter monthly expense: "))
income = int(input("Enter monthly income: "))

if expense > income:
    print("Overspending! Need to cut down")
elif expense == income:
    print("Breaking even")
else:
    savings = income - expense
    print("Good! You saved:", savings)
