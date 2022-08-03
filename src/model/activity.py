from src.model import db
from src.model.timestamp import TimeStampModel


class ActivityModel(db.Model, TimeStampModel):
    __tablename__ = "activities"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
