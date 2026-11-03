balance = 3000
names = ["Daily", "Weekly", "Monthly"]
mb = [[100, 200], [750, 1500], [3000, 5000]]
price = [[100, 200], [500, 1000], [1500, 2500]]

while True:
    code = input("Dial: ")
    if code == "*312#":
        break
    print("Invalid USSD code. Try again.\n")

done = False

while not done:
    print("\nMTN Data Plans")
    for i in range(3):
        print(i + 1, names[i])
    print("0 Exit")
    choice = input("Reply: ")

    if choice == "0":
        print("Session ended.")
        break
    if choice not in ["1", "2", "3"]:
        print("Invalid choice.")
        continue
    c = int(choice) - 1

    while True:
        print("\n" + names[c] + " Plans")
        for i in range(2):
            print(i + 1, str(mb[c][i]) + "MB - N" + str(price[c][i]))
        print("0 Back")
        plan = input("Reply: ")

        if plan == "0":
            break
        if plan not in ["1", "2"]:
            print("Invalid choice.")
            continue
        p = int(plan) - 1

        while True:
            print("\nBuy " + str(mb[c][p]) + "MB for N" + str(price[c][p]) + "?")
            print("1 Yes")
            print("2 No")
            confirm = input("Reply: ")

            if confirm == "1":
                if price[c][p] > balance:
                    print("Insufficient airtime balance.")
                else:
                    balance = balance - price[c][p]
                    print("\nYou have successfully purchased " + str(mb[c][p]) + "MB of data")
                    print("Airtime balance: N" + str(balance))
                    done = True
                break
            elif confirm == "2":
                break
            else:
                print("Invalid choice.")

        if done:
            break
