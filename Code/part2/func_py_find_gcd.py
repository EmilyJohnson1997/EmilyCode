# func_py_find_gcd.py
def func_py_find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
