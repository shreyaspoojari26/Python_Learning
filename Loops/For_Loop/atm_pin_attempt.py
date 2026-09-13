correct_pin = "1234"

for attempt in range(3):

    pin = input("Enter PIN: ")

    if pin == "":
        continue

    if pin == correct_pin:
        print("Access granted")
        break

    print("Wrong PIN")
