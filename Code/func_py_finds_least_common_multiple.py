# func_py_find_least_common_multiple.py
def func_py_find_least_common_multiple(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)

print(func_py_find_least_common_multiple(12, 15))
