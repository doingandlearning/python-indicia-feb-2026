# - Create a function `calculate_shipping(subtotal, shipping_method="standard", free_shipping_threshold=50.0)` that:
#   - Takes subtotal and optional shipping_method and free_shipping_threshold
#   - If subtotal >= free_shipping_threshold, returns 0 (free shipping)
#   - Otherwise, returns shipping cost based on method:
#     - "standard": £3.99
#     - "express": £7.99
#     - "overnight": £12.99

# calculate_shipping(5) -> 3.99
from function import calculate_shipping

def test_shipping_with_low_cost_comes_back_with_standard_rate():
  assert calculate_shipping(5) == 3.99

# calculate_shipping(5, "express") -> 7.99
def test_shipping_with_low_cost_and_express_comes_back_right():
  assert calculate_shipping(5, "express") == 7.99

def test_shipping_with_low_cost_and_overnight_comes_back_right():
  assert calculate_shipping(5, "overnight") == 12.99

def test_shipping_above_50_should_give_0():
  assert calculate_shipping(100) == 0

def test_shipping_above_set_max_should_give_0():
  assert calculate_shipping(10, free_shipping_threshold=5) == 0