# func_get_n_largest_elements.py
def func_get_n_largest_elements(lst, n):
    return sorted(lst, reverse=True)[:n]

print(func_get_n_largest_elements([1, 3, 5, 2, 4, 6], 3))
