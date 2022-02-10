class Account:
    """ Class for accounts """

    """Method for account object instantiation"""
    def __init__(self, customer_id, acc_num, acc_type="Debit", balance=0.0):
        self.balance = balance
        self.customer_id = customer_id
        self.acc_type = acc_type
        self.acc_number = acc_num

    """Methods to represent the class object as a string"""
    def __str__(self):
        return f"Account number: {self.acc_number}, Type: {self.acc_type}, Balance: {self.balance}"

    def __repr__(self):
        return f"Account(customer_id={self.customer_id}, acc_num={self.acc_number}, acc_type={self.acc_type}, " \
               f"balance={self.balance})"
