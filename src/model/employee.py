from src.model import db, datetime, func
from src.model.timestamp import TimeStampModel


class EmployeeModel(db.Model, TimeStampModel):
    __tablename__ = 'employees'

    id = db.Column(db.String(10), primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)

    def generate_employee_id(self):
        max_employee_id = self.query(func.max(self.id)).filter_by(
            created_at=datetime.now()).first()

        print(max_employee_id)

        year = str(datetime.now().year)
        month = str(datetime.now().month).zfill(2)

        if not max_employee_id:
            max_employee_id = '0001'
        else:
            max_employee_id = int(max_employee_id[-4:]) + 1
            max_employee_id = str(max_employee_id).zfill(4)

        print(max_employee_id)

        employee_id = year + month + max_employee_id
        return employee_id

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.id = self.generate_employee_id()
