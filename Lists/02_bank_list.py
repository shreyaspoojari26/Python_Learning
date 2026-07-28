  """ Bank List"""
name=input("enter bank account holder name:")
account_number=input("enter bank account number:")
bank_balance=int(input("enter the amount:"))
"""
name=("Shreyas")
account_number=(81820100012030)
bank_balance=(1000)
"""
withdrawal=input("enter amount to be withdraw:")
Bank_Balance=(bank_balance-int(withdrawal))
print("remaining amount",Bank_Balance)
Deposite=input("enter amount to be deposit:")
Bank_Balance=(Bank_Balance+int(Deposite))
print("Total amount",Bank_Balance)
print("updated balance",Bank_Balance)
