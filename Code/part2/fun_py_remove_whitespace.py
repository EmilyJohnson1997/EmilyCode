# fun_py_remove_whitespace.py

def fun_py_remove_whitespace(s):
    return "".join(s.split())

def test_remove_whitespace():
    text = "  Hello   World  "
    print(f"Without whitespace: {fun_py_remove_whitespace(text)}")

if __name__ == "__main__":
    test_remove_whitespace()
