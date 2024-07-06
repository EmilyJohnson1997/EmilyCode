# fun_find_min_max.py
def find_min_max(lst):
    return min(lst), max(lst)

lst = [3, 5, 1, 9, 2]
min_val, max_val = find_min_max(lst)
print(f"Min: {min_val}, Max: {max_val}")
