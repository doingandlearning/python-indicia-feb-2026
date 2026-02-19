    # Create a function calculate_subtotal(items) that:
    #     Takes a list of tuples where each tuple is (product_name, price, quantity)
    #     Uses a for loop to iterate through the items
    #     For each item, multiplies price * quantity and adds to a total
    #     Returns the subtotal as a float

# [(product_name, price, quantity)]
def calculate_subtotal(items):
  """
  Calculates the subtotal - data must be in the form of
  [(product_name, price, quantity)] 
  """
  subtotal = 0

  for _, price, quantity in items:
    subtotal += price * quantity

  return subtotal

# TDD -> fails (red) -> pass (green) -> improve (refactor) 
print(f'Actual answer: £{calculate_subtotal([("Cups", 5.00, 5), ("Plates", 10, 3)])}')  # 
print("Real answer: £55")

# Create apply_promotion_code(price, promo_code):

#     Check if promo_code matches valid codes:
#         “SAVE10”: 10% discount
#         “SAVE20”: 20% discount
#         “FREESHIP”: no discount (return 0 for now)
#     If code is invalid, return original price
#     Return a tuple: (discounted_price, discount_amount)

def get_discounted_price(original_price, percentage_discount):
  discount_amount = original_price * percentage_discount 
  discounted_price = original_price - discount_amount
  return (discounted_price, discount_amount)  

def apply_promotion_code(original_price, discount_code):
  if discount_code == "SAVE10":
    return get_discounted_price(original_price, 0.1)
  elif discount_code == "SAVE20":
    return get_discounted_price(original_price, 0.2) 
  elif discount_code == "SAVE30":
    return get_discounted_price(original_price, 0.3) 
  elif discount_code == "FREESHIP":
    return (0, original_price)
  return (original_price, 0)

print(f"{apply_promotion_code(10, "SAVE10")} should return (9, 1)")
print(f"{apply_promotion_code(10, "SAVE20")} should return (8, 2)")
print(f"{apply_promotion_code(10, "FREESHIP")} should return (0, 10)")
print(f"{apply_promotion_code(10, "INVALID")} should return (10, 0)")