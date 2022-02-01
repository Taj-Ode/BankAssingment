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
        self.customers = []
        self.accounts = []
        self._load()

    def _load(self):
        self.customers.append(self.ds.get_customers())
        self.accounts = self.ds.get_accounts()

        # with open(DataSource.customer_data_path, 'r') as customerData:
        #     for line in customerData:
        #         Bank.all_data = (line.strip('\n').split(':'))
        #         customer_array = Bank.all_data[:3]
        #         self.customers.append(customer_array)
        #         accounts_array = ':'.join(Bank.all_data[3:]).split('#')
        #         self.accounts.append(accounts_array)
        #     return Bank.all_data

    def get_customers(self):
        return self.customers

    def get_customer(self, pnr):
        for customer in self.customers:
            if pnr == customer[2]:
                return customer
        return None, "That customer doesn't exist"

    def get_accounts(self):
        for customer_accounts in self.accounts:
            n = len(customer_accounts)
            n_split = np.array_split(customer_accounts, n)
            for single_account in n_split:
                (list(single_account))

    # def get_account(self, acc_nr):
    #     for account in single_accounts


nordea = Bank()
print(nordea.get_customers())
# print('\n')
# print(nordea.get_customer('19920612-2385'))
# print(nordea.get_customer('19881011-2394'))
#
# print(nordea.get_customer('19'))
# print('\n')
# print(nordea.get_accounts())


