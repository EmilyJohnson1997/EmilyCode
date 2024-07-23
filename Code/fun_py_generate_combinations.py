# fun_py_generate_combinations.py
from itertools import combinations

def fun_py_generate_combinations(lst, r):
    return list(combinations(lst, r))

print(fun_py_generate_combinations([1, 2, 3], 2))
