#utility
def valid_date(start_date, end_date):
    start_date  = start_date[8:]
    end_date = end_date[8:]
    number_of_days_of_leave = end_date - start_date
    if(number_of_days_of_leave > 14):
        return "maximum consecutive leave days is 14"
    else:
        return number_of_days_of_leave
