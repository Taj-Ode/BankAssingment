from Customer import Customer
from Account import Account
from pathlib2 import Path


class DataSource:
    """ Data Source class"""

    customer_data_path = "C:\\Users\\Tajia\\Handels\\Artificiell Intelligence 1\\Assignments\\BankAssingment2701\\BankAssingment\\customerdata.txt"

    @staticmethod
    def datasource_conn(path):
        """Initial file connection"""
        try:
            with open(path, 'r'):
                return True, "Connection successful", path
        except:
            return False, "Connection unsuccessful"

    @staticmethod
    def get_customer_list():
        data_list = []
        customer_list = []
        with open(DataSource.customer_data_path, 'r') as all_data:
            for line in all_data:
                data = line.strip('\n').split(':')
                data_list.append(data)
            for x in data_list:
                customer = Customer(int(x[0]), x[1], x[2])
                customer_list.append(customer)
        return customer_list

    @staticmethod
    def get_accounts_list():
        accounts_list = []
        with open(DataSource.customer_data_path, 'r') as all_data:
            for line in all_data:
                temp_list = line.strip('\n').split(':')
                customer_id = int(temp_list[0])
                data_list = ','.join(temp_list[3:]).split('#')
                for x in data_list:  # the accounts for each customer (each line)
                    account_items = x.split(',')
                    acc_num = int(account_items[0])
                    acc_type = account_items[1]
                    balance = float(account_items[2])
                    account = Account(customer_id, acc_num, acc_type, balance)
                    accounts_list.append(account)
        return accounts_list

    # Below are unused methods meant for VG grade
    # def get_next_customer_id(self):
    #     customer_ids = []
    #     with open(DataSource.customer_data_path, 'r') as all_data:
    #         for lines in all_data:
    #             line = lines.strip().split(":")
    #             customer_ids.append(line[0])
    #         last_id = customer_ids[-1]
    #         next_id = int(last_id) + 1
    #     return next_id
    #
    # def get_next_acc_nr(self):
    #     acc_nrs = []
    #     for account in self.get_accounts_list():
    #         acc_nrs.append(account.acc_number)
    #     last_acc_num = acc_nrs[-1]
    #     next_acc_num = int(last_acc_num) + 1
    #     return next_acc_num
    #
    # def update_name(self, search_text, replace_text):
    #     file = Path(DataSource.customer_data_path)
    #     data = file.read_text()
    #     data = data.replace(search_text, replace_text)
    #     file.write_text(data)
    #     return "Text replaced"
    #
    # def refresh(self):
    #     self.get_customer_list()
    #     self.get_accounts_list()
