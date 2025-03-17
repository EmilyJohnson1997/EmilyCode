# func_py_sum_of_digits.py

def func_py_sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

def test_sum_of_digits():
    numbers = [123, 456, 789]
    for num in numbers:
        print(f"Sum of digits in {num}: {func_py_sum_of_digits(num)}")

if __name__ == "__main__":
    test_sum_of_digits()
