# Product data: (name, price, category, stock, sales)
products = [
    ("Wireless Mouse", 29.99, "Electronics", 50, 120),
    ("USB-C Cable", 12.99, "Electronics", 100, 85),
    ("Desk Lamp", 45.00, "Furniture", 25, 30),
    ("Notebook Set", 18.50, "Stationery", 75, 45),
    ("Keyboard", 79.99, "Electronics", 30, 60),
    ("Monitor Stand", 35.00, "Furniture", 40, 25),
]  
# p[1] * 1.2
# map    x  =>  y
product_names = []
for product in products:
  product_names.append(product[0])


# Pythonic - Python idiomatic - List Comprehension
product_names = [product[0] for product in products]

# Calculate prices with tax (20%)
prices_with_tax = [round(product[1] * 1.2, 2) for product in products]
print(prices_with_tax)

def calculate_with_tax(price, tax_rate):
  return round(price * (1 + tax_rate), 2)

prices_with_tax = [calculate_with_tax(product[1], 0.2) for product in products]
print(prices_with_tax)

# Display string  (f"{p[0]} - £{p[1]}")
display_strings = [f"{p[0]} - £{p[1]:.2f}" for p in products]
print(display_strings)