# func_py_anagram_check.py

def func_py_anagram_check(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

def test_anagram_check():
    pairs = [("Listen", "Silent"), ("Hello", "Olelh"), ("Apple", "Peach")]
    for s1, s2 in pairs:
        print(f"'{s1}' and '{s2}' are anagrams: {func_py_anagram_check(s1, s2)}")

if __name__ == "__main__":
    test_anagram_check()
