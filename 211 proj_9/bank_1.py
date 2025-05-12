class Bank:
    def __init__(self, name, routing_number, address):
        self.name = name
        self.routing_number = routing_number
        self.address = address
        self.accounts = []
        self.customers = []

    def __str__(self):
        ret_str = f"Bank: {self.name}\n"
        ret_str += f"Routing Number: {self.routing_number}\n"
        ret_str += f"Address: {self.address}\n"
        ret_str += f"Accounts: {', '.join(self.accounts)}\n"
        ret_str += f"Customers: {', '.join(self.customers)}\n"
        return ret_str
    
    def add_account(self, account):
        self.accounts.append(account)
    
    def add_customer(self, customer):
        self.customers.append(customer)


if __name__ == "__main__":
    b = Bank("US Bank", 123456789, "123 Main St")
    b.add_account("123549984")
    b.add_account("5698676778")
    b.add_customer("Alice River")
    b.add_customer("Bob Water")
    print(b)
    print(b.customers)




class Customer:
    def __init__(self, cust_id, name):
        self.cust_id = cust_id
        self.name = name
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        accs = ", ".join(self.accounts)
        return f"Customer {self.name} id {self.cust_id}\n Accounts: {accs}"
    
    
if __name__ == "__main__":
    c = Customer(5, "Alice River")
    c.add_account("123549984")
    c.add_account("5698676778")
    print(c)

