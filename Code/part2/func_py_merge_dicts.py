# func_py_merge_dicts.py

def func_py_merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

def test_merge_dicts():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    print(f"Merged dictionary: {func_py_merge_dicts(dict1, dict2)}")

if __name__ == "__main__":
    test_merge_dicts()
