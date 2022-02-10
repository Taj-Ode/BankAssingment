from Bank import Bank

nordea = Bank()

bank_options = {
    "1": "Print a list of all customers",  # works
    "2": "Print a list of all accounts",  # works
    "3": "Print specific customer",  # works
    "4": "Print specific account",  # works
    "5": "Add a customer",  # works
    "6": "Change a customer name",  # works
    "7": "Add account to a customer",  # works
    "8": "Deposit to a customer account",  # works
    "9": "Withdraw from a customer account",  # works
    "10": "Remove a customer",  # works
    "11": "Remove account from a customer",  # works
    "12": "Exit"
}


def print_menu():
    for key in bank_options.keys():
        print(key, ':', bank_options[key])


while True:
    print_menu()
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print("Wrong input. Please enter a number.")

    if option == 1:
        for x in nordea.get_customers():
            print(x)
        print('\n')
        input("Press enter to return to menu")

    elif option == 2:
        for x in nordea.get_accounts():
            print(x)
        print('\n')
        input("Press enter to return to menu")

    elif option == 3:
        pnr_input = input("Enter personal number: ").strip()
        customer = nordea.get_customer(pnr=pnr_input)
        if customer is not None:  # when the return is a customer
            print(customer)
        else:  # when the return is none
            print("Customer doesn't exist.")
        print("\n")
        input("Press enter to return to menu.")

    elif option == 4:
        pnr_input = input("What is the customer's pnr? ").strip()
        customer = nordea.get_customer(pnr=pnr_input)
        if customer is not None:
            acc_nr = int(input("Which account do you want to see? "))
            account = nordea.get_account(pnr=pnr_input, acc_num=acc_nr)
            if account is not None:
                print(account)
            else:
                print("Account doesn't exist or doesn't belong to this customer.")
        else:
            print("Customer doesn't exist.")
        print("\n")
        input("Press enter to return to menu.")

    elif option == 5:
        name_input = input("What is the customer's name? ").strip()
        pnr_input = input("What is the customer's pnr? ").strip()
        success = nordea.add_customer(name=name_input, pnr=pnr_input)
        if success:
            print("Customer has been added.")
        else:
            print("Customer already exists.")
        print("\n")
        input("Press enter to return to menu.")

    elif option == 6:
        pnr_input = str(input("What is the persons personal number? ")).strip()
        name_input = str(input("What is the new name? ")).strip()
        success = nordea.change_customer_name(pnr=pnr_input, new_name=name_input)
        if success:
            print("Name change successful.")
        else:
            print("Customer not found.")
        print("\n")
        input("Press enter to return to menu.")

    elif option == 7:
        pnr_input = input("What is the customer's pnr? ").strip()
        customer = nordea.get_customer(pnr=pnr_input)
        success = nordea.add_account(pnr=pnr_input)
        if success:
            print("Account has been added to {}".format(customer))
        else:
            print("Customer not found. Account not added.")
        print("\n")
        input("Press enter to return to menu.")

    elif option == 8:
        pnr_input = input("What is the customer's pnr? ").strip()
        customer = nordea.get_customer(pnr=pnr_input)
        if customer is not None:
            acc_nr = int(input("Which account do you want to deposit to? "))
            account = nordea.get_account(pnr=pnr_input, acc_num=acc_nr)
            if account is not None:
                amount = float(input("How much do you want to deposit?"))
                balance = nordea.deposit(pnr=pnr_input, acc_num=acc_nr, amount=amount)
                print("You deposited {0} kr and your balance is now {1}".format(amount, balance))
            else:
                print("Account doesn't exist or doesn't belong to this customer. Deposit not successful.")
        else:
            print("Customer doesn't exist.")
        print("\n")
        input("Press enter to return to menu.")

    elif option == 9:
        pnr_input = input("What is the customer's pnr? ").strip()
        customer = nordea.get_customer(pnr=pnr_input)
        if customer is not None:
            acc_nr = int(input("Which account do you want to withdraw from? "))
            account = nordea.get_account(pnr=pnr_input, acc_num=acc_nr)
            if account is not None:
                amount = float(input("How much do you want to withdraw?"))
                balance = nordea.withdraw(pnr=pnr_input, acc_num=acc_nr, amount=amount)
                if balance:
                    print("You withdrew {0} kr and your balance is now {1}".format(amount, balance))
                else:
                    print("Insufficient funds.")
            else:
                print("Account doesn't exist or doesn't belong to this customer. Withdrawal not successful.")
        else:
            print("Customer doesn't exist.")
        print("\n")
        input("Press enter to return to menu.")

    elif option == 10:  # implement remove all accounts too
        pnr_input = str(input("What is the customer's personal number? ")).strip()
        success = nordea.remove_customer(pnr=pnr_input)
        if success:
            print("Customer removed. Balance returned is {}".format(success))
        else:
            print("Customer not found.")
        print("\n")
        input("Press enter to return to menu.")

    elif option == 11:
        pnr_input = str(input("What is the customer's personal number? ")).strip()
        customer = nordea.get_customer(pnr=pnr_input)
        if customer is not None:
            acc_nr = int(input("Which account do you want to close? "))
            account = nordea.get_account(pnr=pnr_input, acc_num=acc_nr)
            if account is not None:
                success = nordea.close_account(pnr=pnr_input, acc_num=acc_nr)
                if success:
                    print("{0} was deleted from {1}. Returned balance is {2}".format(account, customer, account.balance))
            else:
                print("Account doesn't exist.")
        else:
            print("Customer doesn't exist.")
        print("\n")
        input("Press enter to return to menu.")

    elif option == 12:
        print('Thank you for using Nordea Bank. You will now exit.')
        exit()
    else:
        print('Invalid option. Please enter a number between 1-12.')
        print("\n")
        input("Press enter to return to menu.")
