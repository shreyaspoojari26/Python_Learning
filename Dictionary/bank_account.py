#Bank Account Related 
account = {"name": "Arun", "balance": 10000}

account.update({"balance": 15000, "type": "Savings"})

print(account)
print(account.get("name"))
print(account.get("balance"))
print(account.get("type"))
print(account.keys())
print(account.values())
