# func_py_generate_palindromic_numbers.py
def func_py_generate_palindromic_numbers(n):
    return [i for i in range(1, n + 1) if str(i) == str(i)[::-1]]

print(func_py_generate_palindromic_numbers(200))
