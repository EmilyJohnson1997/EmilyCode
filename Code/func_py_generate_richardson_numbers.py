# func_py_generate_richardson_numbers.py
def func_py_generate_richardson_numbers(limit):
    richardson_numbers = []
    for n in range(1, limit + 1):
        r_n = sum([1 / i for i in range(1, n + 1)])
        if r_n.is_integer():
            richardson_numbers.append(n)
    return richardson_numbers

print(func_py_generate_richardson_numbers(100))
