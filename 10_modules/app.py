# import numpy as np
# import pandas as pd
from .utils import insecure_printer as printer, Shape   # importing parts of the module -> not namespaced
# namespacing -> 
import os

# print(os.cpu_count())

# from random import choice

# print(choice(["Heads", "Tails"]))


# print(u.triangle.type)

# u.insecure_printer("Hello from app.py")

# circle = u.Shape("circle")
# print(circle.type)

# printer("I was imported and not namespaced")

print(__name__)
print(u.__name__)
# print(__file__)
# print(__doc__)
# print(dir(u))

# public_names = [name for name in dir(u) if not name.startswith("_")]
# print(public_names)

# standalone code ✅
# packages ✅
# __pycache__ ✅
# third party libraries