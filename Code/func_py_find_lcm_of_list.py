# func_py_find_lcm_of_list.py
def func_py_find_lcm_of_list(lst):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return abs(x * y) // gcd(x, y)

    lcm_val = lst[0]
    for num in lst[1:]:
        lcm_val = lcm(lcm_val, num)

    return lcm_val

print(func_py_find_lcm_of_list([12, 15, 20]))
