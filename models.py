#Using sqlalchemy

from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class Leave(db.Model):
    employee_id = db.Column(db.String, primary_key = True)
    start_date = db.Column(db.String, nullable = False)
    end_date = db.Column(db.String, nullable = False)
    reason_for_leave = db.Column(db.String, nullable = False)
    leave_type = db.Column(db.String, nullable = False)



