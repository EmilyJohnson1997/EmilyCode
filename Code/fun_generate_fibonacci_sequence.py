# fun_generate_fibonacci_sequence.py
def fun_generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print(fun_generate_fibonacci_sequence(10))
