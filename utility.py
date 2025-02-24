from datetime import datetime

def valid_date(start_date, end_date):
    number_of_days_of_leave = (end_date - start_date).days
    return number_of_days_of_leave