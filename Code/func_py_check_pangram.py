# func_py_check_pangram.py
import string

def func_py_check_pangram(sentence):
    return set(string.ascii_lowercase) <= set(sentence.lower())

print(func_py_check_pangram("The quick brown fox jumps over the lazy dog"))
print(func_py_check_pangram("Hello world"))
