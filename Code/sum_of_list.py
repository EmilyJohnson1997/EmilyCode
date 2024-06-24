# sum_of_list.py
def sum_of_list(numbers):
    return sum(numbers)

if __name__ == "__main__":
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    total = sum_of_list(numbers)
    print(f"The sum of the list is: {total}")
