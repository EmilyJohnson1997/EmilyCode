# func_py_generate_cartesian_product.py
from itertools import product

def func_py_generate_cartesian_product(lst1, lst2):
    return list(product(lst1, lst2))

print(func_py_generate_cartesian_product([1, 2, 3], ['a', 'b', 'c']))
