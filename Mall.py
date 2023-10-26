class Shopping_Mall:
    def __init__(self, name) -> None:
        self.name = name 
        self.sellers = {}
        self.customers = {}
    
    def profile(self):
        return f"Name: {self.name}\nTotal Sellers: {len(self.sellers)}\nTotal Customer: {len(self.customers)}"

    def add_seller(self, seller):
        self.sellers[seller] = seller.name
    
    def add_customer(self, customer):
        self.customers[customer] = customer.name 
