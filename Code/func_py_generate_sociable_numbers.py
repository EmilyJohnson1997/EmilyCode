# func_py_generate_sociable_numbers.py
def func_py_generate_sociable_numbers(limit, cycle_length):
    def sum_of_divisors(num):
        return sum(i for i in range(1, num) if num % i == 0)
    
    sociable_numbers = []
    for n in range(2, limit):
        chain = [n]
        for _ in range(cycle_length):
            n = sum_of_divisors(n)
            if n in chain:
                break
            chain.append(n)
        if len(chain) == cycle_length and chain[-1] == chain[0]:
            sociable_numbers.append(chain)
    
    return sociable_numbers

print(func_py_generate_sociable_numbers(10000, 5))
