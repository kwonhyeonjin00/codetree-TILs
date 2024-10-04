class Product:
    def __init__(self, name="", number=0):
        self.name = name
        self.number = number

product1 = Product()

product1.name = "codetree"
product1.number = 50

name, number = input().split()
Product2 = Product(name, number)

print(f'product {product1.number} is {product1.name}')
print(f'product {Product2.number} is {Product2.name}')