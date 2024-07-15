# func_generate_multiples.py
def func_generate_multiples(number, count):
    return [number * i for i in range(1, count + 1)]

print(func_generate_multiples(3, 5))
