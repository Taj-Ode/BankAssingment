from Customer import Customer


class DataSource:
    """ Data Source class"""

    customer_data_path = "C:\\Users\\Tajia\\Handels\\Artificiell Intelligence 1\\Assignments\\BankAssingment2701\\BankAssingment\\customerdata.txt"

    def __init__(self):
        self.datasource_conn(DataSource.customer_data_path)
        self.datasource_list = []
        self.accounts = []
        self.loaded = False


    @staticmethod
    def datasource_conn(path):
        """Initial file connection"""
        try:
            with open(path, 'r'):
                return True, "Connection successful", path
        except:
            return False, "Connection unsuccessful"

    def get_all(self):
        if not self.loaded:
            with open(DataSource.customer_data_path, 'r') as customerData:
                for line in customerData:
                    self.datasource_list = (line.strip('\n').split(':'))
            self.loaded = True
        return self.datasource_list

    def get_customers(self):
        temp_list = self.get_all()
        self.datasource_list = map(lambda c: Customer(c[1], c[2]), customerData)


    def get_accounts(self):
        accounts_array = ':'.join(self.datasource_list[3:]).split('#')
        print(accounts_array)


db = DataSource()
print(db.datasource_conn(DataSource.customer_data_path))
print(db.get_all())
# print(db.get_customers())
# print(db.get_accounts())





# test = DataSource()
# test.get_all()

#customer_array = self.datasource_list[:3]
#print(customer_array)