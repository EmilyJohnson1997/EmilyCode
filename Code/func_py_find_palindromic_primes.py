# func_py_find_palindromic_primes.py
def func_py_find_palindromic_primes(limit):
    primes = []
    for num in range(2, limit):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            if str(num) == str(num)[::-1]:
                primes.append(num)
    return primes

print(func_py_find_palindromic_primes(1000))
