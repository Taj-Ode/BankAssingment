import numpy as np
from Account import Account
from Customer import Customer
from DataSource import DataSource


class Bank:
    """Class for the bank containing all necessary functions"""

    customer_data_path = "C:\\Users\\Tajia\\Handels\\Artificiell Intelligence 1\\Assignments\\BankAssingment2701\\BankAssingment\\customerdata.txt"
    all_data = []
    """ Initialize bank object and populate list of customers and account from txt file. NOT IMPLEMENTED"""

    def __init__(self):
        self.ds = DataSource()
        self._load()

    def _load(self):
        return self.ds.parse_datasource()

    def get_customers(self):
        print(self.ds.customers)

    def get_customer(self, pnr):
        for customer in self.ds.customers:
            if pnr == customer[2]:
                return customer
        return "That customer doesn't exist"

    def change_customer_name(self, name, pnr):
        for customer in self.ds.customers:
            if name == customer[1] and pnr == customer[2]:
                new_name = input("What name do you want to change to? ")
                self.ds.update_file(search_text=name, replace_text=new_name)
                self.ds.refresh()
                return "name change successful"
        return "pnr or name is wrong. Couldn't find customer."

    def get_accounts(self):
        for customer_accounts in self.ds.accounts:
            n = len(customer_accounts)
            n_split = np.array_split(customer_accounts, n)
            for single_account in n_split:
                print(list(single_account))

    # def get_account(self, acc_nr):
    #     for account in self.ds.accounts:
    #         if acc_nr ==

# pnr = '2'
# nordea = Bank()
# print(nordea.get_customers())
# print('\n')
# print(nordea.get_customer(pnr))
# print(nordea.get_customer('19881011-2394'))
# print(nordea.get_customer('19'))
# print('\n')
# print(nordea.get_accounts())
# print(nordea.remove_customer('19881003-2386'))

