import datetime

def days_left_in_month():
    # Get today's date
    today = datetime.date.today()

    # Get the first day of the next month
    first_day_next_month = datetime.date(today.year, today.month + 1, 1) if today.month < 12 else datetime.date(today.year + 1, 1, 1)

    # Calculate the number of days until the first day of the next month
    days_left = (first_day_next_month - today).days

    return days_left

date_str = input("Enter today's date (in DD format): ")
day = int(date_str)

days_left = days_left_in_month()

print(f"There are {days_left} days left in the current month.")
