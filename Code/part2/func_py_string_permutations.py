# func_py_string_permutations.py

from itertools import permutations

def func_py_string_permutations(s):
    return ["".join(p) for p in permutations(s)]

def test_string_permutations():
    words = ["abc", "dog", "xyz"]
    for word in words:
        print(f"Permutations of '{word}': {func_py_string_permutations(word)}")

if __name__ == "__main__":
    test_string_permutations()
