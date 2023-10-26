class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email 
        self.password = password 
        self.wallet = 0
        
    def user_profile(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPassword: {self.password}"
    
    def balance(self):
        return self.wallet 

class Customer(User):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
        self.cart = {}
        self.bill = 0
    
    def load_cash(self, amount):
        self.wallet += amount 
    
    def add_to_cart(self, product):
        self.bill += product.price
        if product in self.cart:
            self.cart[product] += 1
        else:
            self.cart[product] = 1
    
    def remove_from_cart(self, product):
        self.bill -= self.cart[product] * product.price
        self.cart.pop(product)
    
    def pay_bill(self):
        if self.wallet >= self.bill:
            self.wallet -= self.bill 
        else:
            print(f"Payment Unsecussful!\nYou have not sufficient balance for paying {self.bill} taka!")
    
    def show_products(self, shopping_mall, seller=None):
        # todo: 1. I have to show products accorgint to seller name
        #       2. I have to show all seller products by defaut
        print(shopping_mall.sellers)
        if seller is None:
            # show the available products in the stock of all sellers
            for sel in shopping_mall.sellers:
                for product in sel.products.keys():
                    if product.publish == True:
                        print(f"Product: {product.name} Price: {product.price} taka")
        else:
            if seller in shopping_mall.sellers:
                for product in seller.products.keys():
                    if product.publish == True:
                        print(f"Product: {product.name} Price: {product.price} taka")
            else:
                print(f"Sorry! There is no seller by the name of {seller.name} on this mall!")
            

class Seller(User):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
        self.products = {}
    
    def add_product(self, product, quantity):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity
    
    def show_products(self):
        for product in self.products.keys():
            print(f"Name: {product.name} Stock: {self.products[product]} Publish: {product.publish}")
    
    def receive_order(self, order_cart, bill):
        self.wallet += bill 
        for order in order_cart:
            self.products[order] -= order_cart[order]
    



