# func_py_email_validator.py
import re

def func_py_email_validator(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

print(func_py_email_validator("test@example.com"))
