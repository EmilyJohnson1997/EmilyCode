# func_py_vowel_count.py

def func_py_vowel_count(text):
    return sum(1 for char in text.lower() if char in 'aeiou')

def test_vowel_count():
    print(f"Number of vowels in 'hello world': {func_py_vowel_count('hello world')}")

if __name__ == "__main__":
    test_vowel_count()
