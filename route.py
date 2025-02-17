# Routes
from flask import Flask, request, response
from service import process_leave_request
from app import app
from models import Leave
from models import db

@app.route('api/v1/leave_request', method = ["post"])
def leave_request():
    start_date = request.form['start_date']
    end_date = request.form["end_date"]
    request_type = request.form["reason"]
    reason_for_leave = request.form["reason_for_leave"]


    validation_result = process_leave_request(start_date, end_date,request_type,reason_for_leave)

    response_object = Leave(employee_id = "LR001", start_date = start_date, end_date = end_date, leave_type = request_type, reason_for_leave = reason_for_leave , status = validation_result.get("status"),created_at = validation_result.get("created_at") )
    
    try:
        db.session.add(response_object)
        db.session.commit()
        return response.to_dict()
    except:
        return {"message": "Invalide request", "details":["end_date must be after start_date", 
"maximum consecutive leave days is 14" ]}


@app.route(' GET /api/v1/leave-requests/<int: id>', method = ["GET"])
def get_leave_request(id):
    details = Leave.get_or_404(id)
    


