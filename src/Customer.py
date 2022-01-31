from Account import Account
import itertools


class Customer:
    """ Class for customers"""

    customer_id_iterator = itertools.count(start=1, step=1)

    """Method for customer object instantiation"""
    def __init__(self, name, pnr):
        self.name = name
        self.personal_number = str(pnr)
        self.accounts = []
        self.customer_id = next(Customer.customer_id_iterator)

    def change_name(self, new_name):
        old_name = self.name
        self.name = new_name
        print("Previous name: {0} has been changed to: {1}".format(old_name, self.name))

    def print_information(self):
        print("Customer: {0}, {1}, {2}".format(self.customer_id, self.name, self.personal_number))
        for account in self.accounts:
            print("Account: {0}".format(account.get_information()))

    def add_account(self):
        balance = float(input("How much do you want to open this account with? "))
        new_account = Account(balance)
        self.accounts.append(new_account)
        print("A new account has been created: \n"
              "Account number is: {0} \n"
              "Account type is: {1} \n"
              "Account balance is: {2}".format(new_account.account_number, new_account.account_type,
                                               new_account.balance))

    # TODO DOES NOT WORK. NEEDS TO BE FIXED AND COMPLETED
    def remove_account(self):
        balance = 0

        self.print_information()
        acc_to_remove = int(input("Which account do you want to remove from the list above? "))
        for account in self.accounts:
            if acc_to_remove == account.account_number:
                index_of_acc_to_remove = self.accounts.index(account)
                self.accounts.pop(index_of_acc_to_remove)
            else:
                "That account doesn't exist."


bryce = Customer("Bryce Wayne", 199601011212)
bryce.add_account()
bryce.add_account()
print(bryce.print_information())

bryce.remove_account()
print(bryce.print_information())

# tajiana = Customer("Tajiana Odero", 200008140000)
# print(tajiana.print_information())
# elin = Customer("Elin Morgensen", 199505025656)
# print(elin.print_information())