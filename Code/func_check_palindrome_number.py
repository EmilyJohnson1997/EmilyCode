# func_check_palindrome_number.py
def func_check_palindrome_number(num):
    return str(num) == str(num)[::-1]

print(func_check_palindrome_number(121))
print(func_check_palindrome_number(123))
