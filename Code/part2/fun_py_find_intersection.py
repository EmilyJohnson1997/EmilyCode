# fun_py_find_intersection.py

def fun_py_find_intersection(list1, list2):
    return list(set(list1) & set(list2))

def test_find_intersection():
    a = [1, 2, 3, 4, 5]
    b = [4, 5, 6, 7, 8]
    print(f"Intersection: {fun_py_find_intersection(a, b)}")

if __name__ == "__main__":
    test_find_intersection()
