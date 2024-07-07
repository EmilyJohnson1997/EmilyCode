# fun_count_vowels.py
def fun_count_vowels(string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char in vowels)

print(fun_count_vowels('Hello World'))
