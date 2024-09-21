# billing system at super market
while True:
    name = input("Enter customers name: ")
    total = 0
    while True:
        print("enter the amount and quantity")
        amount = float(input("enter amount: "))
        quantity = float(input("enter quantity: "))
        total += amount * quantity
        repeat = input("do you want to add more items? (yes/no)")
        if repeat == "no" or repeat == "No":
            break
    print("-" * 40)
    print(f"Name: {name}")
    print(f"Amount to be paid: ", total)
    print("-" * 40)
    print("**********Happy Shopping*********")

    repeat1 = input("Next customer?(y/n")
    if repeat1 == "no" or repeat1 == "No":
        break
