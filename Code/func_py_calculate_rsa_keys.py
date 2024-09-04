# func_py_calculate_rsa_keys.py
from sympy import isprime, mod_inverse

def func_py_calculate_rsa_keys(p, q):
    assert isprime(p) and isprime(q), "p and q must be prime."
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Common choice for e
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

print(func_py_calculate_rsa_keys(61, 53))
