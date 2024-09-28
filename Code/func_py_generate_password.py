# func_py_generate_password.py
import random
import string

def func_py_generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

print(func_py_generate_password(10))
