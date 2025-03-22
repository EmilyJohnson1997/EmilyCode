# fun_py_fibonacci.py

def fun_py_fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def test_fibonacci():
    print(f"Fibonacci sequence: {fun_py_fibonacci(10)}")

if __name__ == "__main__":
    test_fibonacci()
