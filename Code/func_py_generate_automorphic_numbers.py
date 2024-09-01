# func_py_generate_automorphic_numbers.py
def func_py_generate_automorphic_numbers(limit):
    automorphic_numbers = [n for n in range(1, limit + 1) if str(n**2).endswith(str(n))]
    return automorphic_numbers

print(func_py_generate_automorphic_numbers(1000))
