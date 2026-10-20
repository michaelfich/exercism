LEAP_YEAR_DIVISOR = 4
CENTURY_DIVISOR = 100
LEAP_CENTURY_DIVISOR = 400

def leap_year(year):
    if year % LEAP_CENTURY_DIVISOR == 0:
        return True
    elif year % CENTURY_DIVISOR == 0:
        return False
    elif year % LEAP_YEAR_DIVISOR == 0:
        return True
    else:
        return False
