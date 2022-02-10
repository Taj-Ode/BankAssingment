from Account import Account
from Customer import Customer
from DataSource import DataSource


class Bank:
    """Class for the bank containing all necessary functions"""

    """ Initialize bank object and populate list of customers and account from txt file. NOT IMPLEMENTED"""

    def __init__(self):
        self.ds = DataSource()
        self._load()
        self.customers = self.ds.get_customer_list()
        self.accounts = self.ds.get_accounts_list()

    def _load(self):
        return self.ds.datasource_conn(DataSource.customer_data_path)

    def get_customers(self):
        return self.customers

    def get_customer(self, pnr):
        for customer in self.customers:
            if pnr == customer.personal_number:
                return customer
        return None

    def get_accounts(self):
        return self.accounts

    def get_account(self, pnr, acc_num):
        customer = self.get_customer(pnr)
        if customer is not None:
            for account in self.accounts:
                if acc_num == account.acc_number and customer.customer_id == account.customer_id:
                    return account
            else:
                return None
        return None

    def add_customer(self, name, pnr):
        customer = self.get_customer(pnr)
        if customer is None:
            next_customer_id = self.get_next_customer_id()
            self.customers.append(Customer(next_customer_id, name, pnr))
            return True
        else:
            return False

    def change_customer_name(self, pnr, new_name):
        customer = self.get_customer(pnr)
        if customer is not None:
            customer.name = new_name
            return True
        else:
            return False

    def remove_customer(self, pnr):
        total_balance = 0
        acc_to_remove = []

        customer = self.get_customer(pnr)

        for account in self.accounts:
            if customer.customer_id == account.customer_id:
                total_balance += account.balance
                acc_to_remove.append(self.accounts.index(account))

        for index in reversed(acc_to_remove):
            self.accounts.pop(index)

        for customer in self.customers:
            if pnr == customer.personal_number:
                customer_to_remove = self.customers.index(customer)
                self.customers.pop(customer_to_remove)

        return True, total_balance

    def add_account(self, pnr):
        customer = self.get_customer(pnr)
        if customer is not None:
            next_acc_nr = self.get_next_acc_nr()
            self.accounts.append(Account(customer.customer_id, next_acc_nr))
            return True
        return False

    def close_account(self, pnr, acc_num):
        customer = self.get_customer(pnr)
        if customer is not None:
            account = self.get_account(pnr, acc_num)
            if account is not None:
                index_of_acc_to_remove = self.accounts.index(account)
                self.accounts.pop(index_of_acc_to_remove)
                return account.balance
            return False
        return False

    def deposit(self, pnr, acc_num, amount):
        account = self.get_account(pnr, acc_num)
        if account is not None:
            account.balance += amount
            return account.balance
        return False

    def withdraw(self, pnr, acc_num, amount):
        account = self.get_account(pnr, acc_num)
        if account is not None:
            balance = account.balance
            if amount > balance:
                return False
            else:
                account.balance -= amount
                return account.balance
        return False

    def get_next_customer_id(self):
        customer_ids = []
        for customer in self.customers:
            customer_ids.append(customer.customer_id)
        last_id = customer_ids[-1]
        next_id = int(last_id) + 1
        return next_id

    def get_next_acc_nr(self):
        acc_nrs = []
        for account in self.accounts:
            acc_nrs.append(account.acc_number)
        last_acc_num = acc_nrs[-1]
        next_acc_num = int(last_acc_num) + 1
        return next_acc_num
