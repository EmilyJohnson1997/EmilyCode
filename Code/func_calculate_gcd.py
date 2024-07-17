# func_calculate_gcd.py
def func_calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(func_calculate_gcd(48, 18))
