
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from extension import db

class Leave(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    reason_for_leave = db.Column(db.String, nullable=False)
    leave_type = db.Column(db.String, nullable=False)
    working_days = db.Column(db.Integer)
    status = db.Column(db.String, default="Pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Default timestamp

    def to_dict(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "reason_for_leave": self.reason_for_leave,
            "leave_type": self.leave_type,
            "working_days": self.working_days,
            "status": self.status,
            "created_at": str(self.created_at),
        }
