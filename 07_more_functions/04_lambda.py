# anonymous functions -> arrow functions -> callable
# small, throw away functions

# lambda parameter1, parameter2, parameter3: parameter1 + parameter2 + parameter3

def double(x):
  return x * 2

double = lambda x: x * 2

def add(a,b):
  return a + b

add = lambda a, b: a + b

products = [
    ("Wireless Mouse", 29.99, "Electronics", 50, 120),
    ("USB-C Cable", 12.99, "Electronics", 100, 85),
    ("Desk Lamp", 45.00, "Furniture", 25, 30),
    ("Notebook Set", 18.50, "Stationery", 75, 45),
    ("Keyboard", 79.99, "Electronics", 30, 45),
    ("Monitor Stand", 35.00, "Furniture", 40, 25),
] 

def get_price_from_product(product):
  return product[1]

most_expensive = max(products, key=get_price_from_product)
most_expensive = max(products, key=lambda p: p[1])
print(most_expensive)

best_seller = max(products, key=lambda p: p[4])
print(best_seller)

def get_sales_and_price(product):
  return (product[4], -product[1])

products.sort(key=get_sales_and_price)
products.sort(key=lambda p: (p[4], p[1]))

for product in products:
  print(product)

from pprint import pprint
pprint(products)