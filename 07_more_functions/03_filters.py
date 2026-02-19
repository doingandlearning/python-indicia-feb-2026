# Product data: (name, price, category, stock, sales)
products = [
    ("Wireless Mouse", 29.99, "Electronics", 50, 120),
    ("USB-C Cable", 12.99, "Electronics", 100, 85),
    ("Desk Lamp", 45.00, "Furniture", 25, 30),
    ("Notebook Set", 18.50, "Stationery", 75, 45),
    ("Keyboard", 79.99, "Electronics", 30, 60),
    ("Monitor Stand", 35.00, "Furniture", 40, 25),
]  


product_names = []
for product in products:
  if product[2] == "Electronics":
    product_names.append(product[0])

print(product_names)

product_names = [{"name": p[0], "price": p[1]} for p in products if p[2] == "Electronics"]
print(product_names)

# category == Electronics and price > 30
expensive_electronics = [p for p in products if p[2] == "Electronics" and p[1] > 30]
print(expensive_electronics)


total_sales = sum(p[4] for p in products)  # aggregator function
print(total_sales)

net_income = sum(p[4] * p[1] for p in products)
print(net_income)

print(f"{net_income / total_sales:.2f}")