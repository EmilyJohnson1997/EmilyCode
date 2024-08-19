# func_py_generate_palindromic_primes.py
def func_py_generate_palindromic_primes(limit):
    def is_prime(num):
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    
    return [i for i in range(2, limit) if is_prime(i) and str(i) == str(i)[::-1]]

print(func_py_generate_palindromic_primes(1000))
