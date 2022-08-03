from src.model import db
from src.model import datetime


class AttendanceModel(db.Model):
    __tablename__ = 'attendances'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    check_in_time = db.Column(
        db.DateTime, default=datetime.now(), nullable=False)
    check_out_time = db.Column(db.DateTime, onupdate=datetime.now())
