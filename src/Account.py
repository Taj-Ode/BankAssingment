# import Transaction
# import datetime
# import pytz
import itertools


class Account:
    """ Class for accounts """

    account_type = "Debit"
    acc_nr_iterator = itertools.count(start=1000, step=1)
    acc_list = []

    """Method for account object instantiation"""
    def __init__(self, balance):
        self.account_number = next(Account.acc_nr_iterator)
        self.balance = float(balance)

    """Method to represent the class object as a string"""
    def __str__(self):
        return f"{self.account_number} {self.account_type} {self.balance}"

    def get_information(self):
        return self.account_number, self.account_type, self.balance

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        if amount > 0:
            self.balance += amount
            print("You deposited {0} kr and your balance is now {1}".format(amount, self.balance))
            # self.transaction_list.append(pytz.utc.localize(datetime.datetime.utcnow()), amount)
        else:
            print("Please enter a value greater than 0.")

    def withdraw(self):
        amount = float(input("Current Balance is: {} \nEnter amount to be withdrawn:".format(self.balance)))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("You withdrew {0} kr and your balance is now {1}".format(amount, self.balance))
        else:
            print("Insufficient funds")

    def print_balance(self):
        print("Balance is {}".format(self.balance))
