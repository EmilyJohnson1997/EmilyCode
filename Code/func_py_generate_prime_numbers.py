# func_py_generate_prime_numbers.py
def func_py_generate_prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        if func_py_check_prime_number(num):
            primes.append(num)
    return primes

print(func_py_generate_prime_numbers(50))
