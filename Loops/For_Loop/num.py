for num in range(1, 10):
    if num == 5:
        continue  # skip 5
    if num == 8:
        break     # stop loop
    print(num)
else:
    print("Loop finished without break")
