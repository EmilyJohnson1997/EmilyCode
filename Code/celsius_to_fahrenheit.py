# celsius_to_fahrenheit.py
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

if __name__ == "__main__":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is {fahrenheit}°F")
