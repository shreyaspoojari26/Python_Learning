def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error"

choice = input("+, -, *, /: ")
n1 = int(input("Num1: "))
n2 = int(input("Num2: "))

if choice == '+': print(add(n1, n2))
elif choice == '-': print(sub(n1, n2))
elif choice == '*': print(mul(n1, n2))
elif choice == '/': print(div(n1, n2))
