# - Create a function `calculate_shipping(subtotal, shipping_method="standard", free_shipping_threshold=50.0)` that:
#   - Takes subtotal and optional shipping_method and free_shipping_threshold
#   - If subtotal >= free_shipping_threshold, returns 0 (free shipping)
#   - Otherwise, returns shipping cost based on method:
#     - "standard": £3.99
#     - "express": £7.99
#     - "overnight": £12.99

def calculate_shipping(subtotal, shipping_method="standard", free_shipping_threshold=50):
  if subtotal > free_shipping_threshold:
    return 0
  
  if shipping_method == "express":
    return 7.99
  elif shipping_method == "overnight":
    return 12.99
  return 3.99 

