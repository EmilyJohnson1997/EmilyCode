# func_py_generate_permutations.py
from itertools import permutations

def func_py_generate_permutations(lst, r):
    return list(permutations(lst, r))

print(func_py_generate_permutations([1, 2, 3], 2))
