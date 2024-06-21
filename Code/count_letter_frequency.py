# count_letter_frequency.py
from collections import Counter

def count_letter_frequency(s):
    return Counter(s)

string = "hello world"
letter_frequency = count_letter_frequency(string)
print(f"String: {string}")
print(f"Letter Frequency: {letter_frequency}")
