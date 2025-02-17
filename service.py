#Service to be improved and route should make simple, due time constriants i could not so this
from utility import valid_date
from datetime import datetime
from models import Leave

def process_leave_request(start_date, end_date,request_type,request_details):
    working_days =  valid_date(start_date, end_date)

    if working_days > 14:
        return "maximum consecutive leave days is 14"
    
    if start_date > end_date:
        return "end_date must be after start_date", 


    return ({"working_days": working_days, "status":"Pending", "created_at": datetime.date} )

    
