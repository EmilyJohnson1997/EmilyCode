# func_py_lru_cache.py
from functools import lru_cache

@lru_cache(maxsize=128)
def func_py_fib(n):
    if n < 2:
        return n
    return func_py_fib(n-1) + func_py_fib(n-2)

print(func_py_fib(30))
