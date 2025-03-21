# fun_py_sort_list.py

def fun_py_sort_list(lst):
    return sorted(lst)

def test_sort_list():
    numbers = [34, 12, 5, 78, 23]
    print(f"Sorted list: {fun_py_sort_list(numbers)}")

if __name__ == "__main__":
    test_sort_list()
