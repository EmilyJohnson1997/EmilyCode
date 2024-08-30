# func_py_generate_tribonacci_numbers.py
def func_py_generate_tribonacci_numbers(limit):
    tribonacci_numbers = [0, 1, 1]
    for i in range(3, limit):
        tribonacci_numbers.append(tribonacci_numbers[i-1] + tribonacci_numbers[i-2] + tribonacci_numbers[i-3])
    return tribonacci_numbers

print(func_py_generate_tribonacci_numbers(10))
