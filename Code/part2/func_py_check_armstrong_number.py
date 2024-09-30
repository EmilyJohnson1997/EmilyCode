# func_py_check_armstrong_number.py
def func_py_check_armstrong_number(n):
    num_str = str(n)
    num_digits = len(num_str)
    total_sum = sum(int(digit) ** num_digits for digit in num_str)
    return total_sum == n
