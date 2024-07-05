# fun_simple_calendar.py
import calendar

def simple_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        print(week)

simple_calendar(2024, 7)
