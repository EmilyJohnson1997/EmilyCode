def func_py_fibonacci_recursive(n):
    if n <= 1:
        return n
    return func_py_fibonacci_recursive(n-1) + func_py_fibonacci_recursive(n-2)
