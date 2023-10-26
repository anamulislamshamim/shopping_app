class Product:
    def __init__(self, name, price, seller_name, publish_status, discount=0) -> None:
        self.name = name 
        self.price = price 
        self.seller_name = seller_name
        self.publish = publish_status 
        self.discount = discount 

    def details(self):
        return f"Product: {self.name} Price: {self.price} Seller: {self.seller_name}"

    def update(self, price=0, publish_status=False, discount=0):
        if price > 0:
            self.price = price 
        if publish_status:
            self.publish = publish_status
        if discount > 0:
            self.discount = discount


class Shirt(Product):
    def __init__(self, name, price, seller_name, publish_status) -> None:
        super().__init__(name, price, seller_name, publish_status)
    
class Pant(Product):
    def __init__(self, name, price, seller_name, publish_status, discount=0) -> None:
        super().__init__(name, price, seller_name, publish_status, discount)

class Shoe(Product):
    def __init__(self, name, price, seller_name, publish_status, discount=0) -> None:
        super().__init__(name, price, seller_name, publish_status, discount)
