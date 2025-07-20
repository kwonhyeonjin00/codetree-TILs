product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Stock:
    def __init__(self, product_name, product_code):
        self.product_name = product_name
        self.product_code =  product_code

stock_1 = Stock("codetree", 50)
stock_2 = Stock(product_name, product_code)

print(f"product {stock_1.product_code} is {stock_1.product_name}")
print(f"product {stock_2.product_code} is {stock_2.product_name}")