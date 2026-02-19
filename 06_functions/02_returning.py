def add(a, b):
  return a + b

print(add(1,2) + add(3,4))

def line_total(price, quantity=1):
  """
  Calcalute line total
  
  :param price: Price in Euro
  :param quantity: The amount of items
  """
  return price * quantity

def subtotal(basket):
  """
  Docstring for subtotal
  
  :param basket: A list of tuples (name_of_item, price_of_item, quantity_of_item)
  """
  total = 0
  for _,price,quantity in basket:
    total += line_total(price, quantity)
  return total

basket = [
  ("Notebook", 2.50, 4),
  ("Pen", 1.20, 3),
  ("Mug", 8.00, 1)
]

print(subtotal(basket))