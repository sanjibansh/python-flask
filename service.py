from utility import valid_date
from datetime import datetime
from models import Leave
from extension import db
from flask import current_app

def process_leave_request_service(data):
    start_date = datetime.strptime(data.get("start_date"), "%Y-%m-%d").date()
    end_date = datetime.strptime(data.get("end_date"), "%Y-%m-%d").date()
    request_type = data.get("leave_type")
    reason_for_leave = data.get("reason_for_leave")

    working_days = valid_date(start_date, end_date)

    if working_days > 14 or working_days < 0:
        return {
            "error": "VALIDATION_ERROR",
            "message": "Invalid request",
            "details": [
                "end_date must be after start_date",
                "maximum consecutive leave days is 14"
            ]
        }, 400  # Error response

    new_leave = Leave(
        employee_id="EMP001",
        start_date=start_date,
        end_date=end_date,
        leave_type=request_type,
        reason_for_leave=reason_for_leave,
        working_days=working_days,
        status="Pending",
        created_at=datetime.utcnow(),
    )

    try:
        with current_app.app_context():  # Ensure db session runs within app context
            db.session.add(new_leave)
            db.session.commit()
            db.session.refresh(new_leave)

        leave_dict = new_leave.to_dict()
        leave_dict.pop("status")
        return leave_dict, 201  # Success response
    except Exception as e:
        return {"error": "DATABASE_ERROR", "message": "Failed to save request", "details": str(e)}, 500

def get_leave_request_service(leave_id):
    leave_request = Leave.query.get_or_404(leave_id)
    leave_dict = leave_request.to_dict()
    return leave_dict
