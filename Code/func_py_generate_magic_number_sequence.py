# func_py_generate_magic_number_sequence.py
def func_py_generate_magic_number_sequence(limit):
    def is_magic(num):
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        return num == 1

    return [num for num in range(1, limit) if is_magic(num)]

print(func_py_generate_magic_number_sequence(100))
