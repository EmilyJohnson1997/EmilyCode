# func_py_generate_amicable_numbers.py
def func_py_generate_amicable_numbers(limit):
    def sum_of_divisors(num):
        return sum(i for i in range(1, num) if num % i == 0)
    
    amicable_numbers = []
    for n in range(2, limit):
        m = sum_of_divisors(n)
        if m > n and sum_of_divisors(m) == n:
            amicable_numbers.append((n, m))
    
    return amicable_numbers

print(func_py_generate_amicable_numbers(1000))
