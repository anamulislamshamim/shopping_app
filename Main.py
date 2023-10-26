from Mall import Shopping_Mall
from Products import Product
from Users import Seller, Customer


def main():
    market = Shopping_Mall("Jamuna")

    seller_1 = Seller('kuddus', 'kuddus@gmail.com', 'abc17')
    product_1 = Product('T-shirt', 650, seller_1.name, True)
    product_2 = Product('Shirt', 850, seller_1.name, True)
    product_3 = Product('Boishakhi Lunghi', 320, seller_1.name, False, 20)
    seller_1.add_product(product_1, 80)
    seller_1.add_product(product_2, 50)
    seller_1.add_product(product_3, 500)

    seller_2 = Seller('abul', 'abul@gmail.com', 'abul17')
    shoe_1 = Product('Bata', 650, seller_1.name, True)
    shoe_2 = Product('Appex', 850, seller_1.name, True)
    shoe_3 = Product('Nagra Juta', 320, seller_1.name, False, 20)
    seller_2.add_product(shoe_1, 80)
    seller_2.add_product(shoe_2, 50)
    seller_2.add_product(shoe_3, 500)

    market.add_seller(seller_1)
    market.add_seller(seller_2)

    # customer
    customer_1 = Customer("sakib", 'sakib@gmail.com', 'sakib117')
    customer_1.show_products(market)




if __name__ == "__main__":
    main()