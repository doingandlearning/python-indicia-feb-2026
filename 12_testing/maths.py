def add(a, b):
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise TypeError("Both arguments should be numbers.")
  if isinstance(a, bool) or isinstance(b, bool):
    raise TypeError("Both arguments should be numbers.") 
  return a + b