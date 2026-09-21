# https://www.codewars.com/kata/602afedfd4a64d0008eb4e6e

MONTHS = {
    1:  {'name': 'January', 'length': 31},
    2:  {'name': 'February', 'length': 28},
    3:  {'name': 'March', 'length': 31},
    4:  {'name': 'April', 'length': 30},
    5:  {'name': 'May', 'length': 31},
    6:  {'name': 'June', 'length': 30},
    7:  {'name': 'July', 'length': 31},
    8:  {'name': 'August', 'length': 31},
    9:  {'name': 'September', 'length': 30},
    10: {'name': 'October', 'length': 31},
    11: {'name': 'November', 'length': 30},
    12: {'name': 'December', 'length': 31},
}

def get_day(day: int, is_leap: bool) -> str: 
    """
    Return a formatted string representing the `day` day of the 
    year, accounting for leap years, such as:
    
        "December, 31"
    """
    month = 1
    days_in_month = MONTHS[month]['length']
        
    while days_in_month < day:
        day -= days_in_month
        month += 1
        days_in_month = 29 if (month == 2 and is_leap) else MONTHS[month]['length']
    
    return f"{MONTHS[month]['name']}, {day}"
