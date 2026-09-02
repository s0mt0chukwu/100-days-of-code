account_details ={
        "name": "John",
        "pin": "1234",
        "account_balance": 50000,
    }

pin = input("Please enter your 4-digit PIN: ")

if pin == account_details["pin"]:

    print(f"\nWelcome, John!\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Change Pin\n5. Exit")
    choice = int(input("What do you want to do? Type 1, 2, 3, 4, or 5: "))

    if choice == 1:
        print(f"Your balance is: {account_details["account_balance"]}")

    elif choice == 2:
        amount = int(input("Enter amount to withdraw "))
        if 0 < amount <= account_details["account_balance"]:
            account_details["account_balance"] -= amount
            print(f"Successful!\nYour new balance is: {account_details["account_balance"]}")
        else:
            print("insufficient funds.")

    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            account_details["account_balance"] += amount
            print(f'Successful!\nYour new balance is: {account_details["account_balance"]}')
        else:
            print("Invalid amount.")

    elif choice == 4:
        confirm_pin = input("confirm pin ")

        if confirm_pin == account_details["pin"]:
            New_pin = input("Enter new pin: ")
            account_details["pin"] = New_pin
            print(f"your pin has been successfully updated")
        else:
            print("Incorrect PIN. Please try again")


    elif choice == 5:
        print("Thank you for using our ATM. Goodbye!")


else:
    print("Incorrect PIN. Access denied.")