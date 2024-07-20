# func_check_armstrong.py
def func_check_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    return num == sum(int(digit) ** num_len for digit in num_str)

print(func_check_armstrong(153))
print(func_check_armstrong(123))
