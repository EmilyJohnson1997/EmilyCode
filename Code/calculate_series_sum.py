def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def main():
    n = 100
    sum_n = calculate_sum(n)
    print(f"The sum of the first {n} natural numbers is: {sum_n}")

if __name__ == "__main__":
    main()
