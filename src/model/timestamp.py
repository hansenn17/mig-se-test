from src.model import datetime
from src.model import db


class TimeStampModel():
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    deleted_at = db.Column(db.DateTime)
