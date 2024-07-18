# func_generate_prime_factors.py
def func_generate_prime_factors(num):
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

print(func_generate_prime_factors(60))
