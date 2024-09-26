# func_py_remove_punctuation.py
import string

def func_py_remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

print(func_py_remove_punctuation("Hello, world! How's it going?"))
