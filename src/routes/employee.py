from flask_restful import Api, reqparse, Resource
from src.model import db
from src.model.employee import EmployeeModel


class Register(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('name', type=str, required=True)

    def post(self):
        try:
            payload = Register.parser.parse_args()

            name = payload['name']

            employee = EmployeeModel(name=name)
            db.session.add(employee)
            db.session.commmit()

        except:
            db.session.rollback()
