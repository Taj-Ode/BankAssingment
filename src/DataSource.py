from Customer import Customer
from pathlib2 import Path


class DataSource:
    """ Data Source class"""

    customer_data_path = "C:\\Users\\Tajia\\Handels\\Artificiell Intelligence 1\\Assignments\\BankAssingment2701\\BankAssingment\\customerdata.txt"

    def __init__(self):
        self.datasource_conn(DataSource.customer_data_path)
        self.datasource_list = []
        self.customers = []
        self.accounts = []
        # self.loaded = False

    @staticmethod
    def datasource_conn(path):
        """Initial file connection"""
        try:
            with open(path, 'r'):
                return True, "Connection successful", path
        except:
            return False, "Connection unsuccessful"

    def parse_datasource(self):
        with open(DataSource.customer_data_path, 'r') as customerData:
            for line in customerData:
                self.datasource_list = line.strip('\n').split(':')
                customer_list = self.datasource_list[:3]
                self.customers.append(customer_list)
                accounts_array = ', '.join(self.datasource_list[3:]).split('#')
                self.accounts.append(accounts_array)

    def update_file(self, search_text, replace_text):
        file = Path(DataSource.customer_data_path)
        data = file.read_text()
        data = data.replace(search_text, replace_text)
        file.write_text(data)
        return "Text replaced"

    def refresh(self):
        self.datasource_list = []
        self.customers = []
        self.accounts = []
        self.parse_datasource()




# db = DataSource()
# print(db.get_all())
# print(db.datasource_conn(DataSource.customer_data_path))
# print(db.accounts)
# print(db.get_accounts())


# test = DataSource()
# test.get_all()

# customer_array = self.datasource_list[:3]
# print(customer_array)
