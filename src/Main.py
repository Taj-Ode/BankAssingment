from Bank import Bank

nordea = Bank()

bank_options = {
    "1": "Print a list of all customers",
    "2": "Print a list of all accounts",
    "3": "See specific customer information",
    "4": "Deposit to a customer account",
    "5": "Withdraw from a customer account",
    "6": "Add a customer",
    "7": "Change a customer name",
    "8": "Remove a customer",
    "9": "Add account to a customer",
    "10": "Remove account from a customer",
    "11": "Exit"
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
        nordea.get_customers()
        print('\n')
        input("Press enter to return to menu")

    elif option == 2:
        nordea.get_accounts()
        print('\n')
        input("Press enter to return to menu")

    elif option == 3:
        pnr = input("Enter personal number: ")
        nordea.get_customer(pnr)
        print("\n")
        input("Press enter to return to menu")

    elif option == 4:
        pass

    elif option == 5:
        pass

    elif option == 6:
        pass

    elif option == 7:
        pass

    elif option == 8:
        pass

    elif option == 9:
        pass

    elif option == 10:
        pass

    elif option == 11:
        print('Thank you for using Nordea Bank. You will now exit.')
        exit()
    else:
        print('Invalid option. Please enter a number between 1-11.')
