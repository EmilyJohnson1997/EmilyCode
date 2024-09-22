# func_py_calculate_factorial.py
def func_py_calculate_factorial(n):
    return 1 if n == 0 else n * func_py_calculate_factorial(n - 1)

print(func_py_calculate_factorial(5))
