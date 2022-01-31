class DataSource:
    """ Data Source class"""

    datasource_list = []
    customer_data_path = "C:\\Users\\Tajia\\Handels\\Artificiell Intelligence 1\\Assignments\\BankAssingment2701\\BankAssingment\\customerdata.txt"

    def __init__(self):
        self.datasource_conn(DataSource.customer_data_path)

    def datasource_conn(self, path):
        """Initial file connection"""
        try:
            with open(path, 'r'):
                return True, "Connection successful", path
        except:
            return False, "Connection unsuccessful"

    def get_all(self):
        with open(DataSource.customer_data_path, 'r') as customerData:
            for line in customerData:
                customer_id_field, name_field, pnr_field, acc_nr_field, acc_type_field, balance_field = tuple(
                    line.strip('\n').split(':'))
                customer_id_field = int(customer_id_field)
                acc_nr_field = int(acc_nr_field)
                balance_field = float(balance_field)
                print(customer_id_field, name_field, pnr_field, acc_nr_field, acc_type_field, balance_field)

test = DataSource()
print(test.datasource_conn(DataSource.customer_data_path))
print(test.get_all())

# TODO def update_by_id(self, customer_id):

# TODO def find_by_id(self, customer_id):

# TODO def remove_by_id(self, customer_id):




