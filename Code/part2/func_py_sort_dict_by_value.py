# func_py_sort_dict_by_value.py
def func_py_sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))

data = {"apple": 5, "banana": 2, "cherry": 8}
print(func_py_sort_dict_by_value(data))
