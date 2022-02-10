class Customer:
    """ Class for customers"""

    """Method for customer object instantiation"""
    def __init__(self, customer_id, name, pnr):
        self.customer_id = customer_id
        self.name = name
        self.personal_number = pnr

    """Method to represent a class object as a string"""
    def __str__(self):
        return f"Id: {self.customer_id} Name: {self.name} Pnr: {self.personal_number}"

    def __repr__(self):
        return f'Customer(customer_id={self.customer_id}, name={self.name}, pnr={self.personal_number})'

