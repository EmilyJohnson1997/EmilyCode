# func_py_find_smith_numbers.py
def func_py_find_smith_numbers(limit):
    def is_prime(n):
        return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

    def digit_sum(n):
        return sum(int(digit) for digit in str(n))
    
    def prime_factors(n):
        i = 2
        factors = []
        while n > 1:
            if n % i == 0:
                factors.append(i)
                n //= i
            else:
                i += 1
        return factors
    
    smith_numbers = []
    for n in range(4, limit):
        if not is_prime(n):
            factors = prime_factors(n)
            if digit_sum(n) == sum(digit_sum(factor) for factor in factors):
                smith_numbers.append(n)
    
    return smith_numbers

print(func_py_find_smith_numbers(500))
