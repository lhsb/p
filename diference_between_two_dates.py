# Difference between two dates in days

m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # days in month

def set_leap(year):
    # set number days of February for given year
    if year % 400 == 0:
        m[1] = 29
    elif year % 100 == 0:
        m[1] = 28
    elif year % 4 == 0:
        m[1] = 29
    else:
        m[1] = 28
    return m

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    
    d = 0
    if year1 != year2: # the years are different
        
        set_leap(year1) # number of days in the first year
        d = sum(m[month1-1:]) - day1
        
        while year1 < year2-1: # number of days in the years between first and last year
            year1 = year1 + 1
            set_leap(year1)
            d = d + sum(m)
        
        set_leap(year2) # number of days in the last year
        d = d + sum(m[:month2-1]) + day2
        
    else: # the years are same
        set_leap(year2)
        mm = sum(m[month1-1:month2-1])
        d = mm - day1 + day2
    return d
