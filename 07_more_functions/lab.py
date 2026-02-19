products = [
    ("Wireless Mouse", 29.99, "Electronics", 50, 120),
    ("USB-C Cable", 12.99, "Electronics", 100, 85),
    ("Desk Lamp", 45.00, "Furniture", 25, 30),
    ("Notebook Set", 18.50, "Stationery", 75, 45),
    ("Keyboard", 79.99, "Electronics", 30, 60),
    ("Monitor Stand", 35.00, "Furniture", 40, 25),
]  

electronics = [p for p in products if p[2] == "Electronics"]

def filter_by_category(products, category):
  return [p for p in products if p[2] == category]

stationary = filter_by_category(products, "Stationery") 
stationary = filter_by_category(products, "Furniture") 