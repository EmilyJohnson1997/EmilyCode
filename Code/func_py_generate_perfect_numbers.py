# func_py_generate_perfect_numbers.py
def func_py_generate_perfect_numbers(limit):
    def is_perfect(num):
        return sum(i for i in range(1, num) if num % i == 0) == num
    
    return [i for i in range(2, limit) if is_perfect(i)]

print(func_py_generate_perfect_numbers(10000))
