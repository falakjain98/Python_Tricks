#! python3
# assert.py - using assert to ensure discounted price is between zero and max price

def apply_discount(product,discount):
    price = int(product['price']*(1.0-discount))
    assert 0 <= price <= product['price'], ('Discounted price cannot be less than 0 or more than original price')
    return price

shoes = {'name': 'Fancy Shoes', 'price': 14900}
apply_discount(shoes,0.25)
apply_discount(shoes,2.0)