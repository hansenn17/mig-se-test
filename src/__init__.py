import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api
from src.model import db
from src.model.activity import ActivityModel
from src.model.employee import EmployeeModel
from src.model.attendance import AttendanceModel


def create_app(test_config=None):
    app = Flask(
        __name__,
        instance_relative_config=True
    )

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get(
                "SQLALCHEMY_TRACK_MODIFICATIONS")
        )
    else:
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app, prefix='/api/v1')

    with app.app_context():
        db.create_all()

    JWTManager(app)

    return app
