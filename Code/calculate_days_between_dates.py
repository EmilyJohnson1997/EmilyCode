# calculate_days_between_dates.py
from datetime import datetime

def days_between_dates(date1, date2):
    delta = date2 - date1
    return delta.days

if __name__ == "__main__":
    date1_str = input("Enter the first date (YYYY-MM-DD): ")
    date2_str = input("Enter the second date (YYYY-MM-DD): ")
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    days = days_between_dates(date1, date2)
    print(f"The number of days between {date1_str} and {date2_str} is: {days}")
