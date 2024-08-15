# func_py_find_perfect_squares.py
def func_py_find_perfect_squares(limit):
    return [i**2 for i in range(1, int(limit**0.5) + 1)]

print(func_py_find_perfect_squares(100))
