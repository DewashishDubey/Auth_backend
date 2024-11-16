from flask import Flask
from settings import settings
from db.base import db as database


def init_database(app : Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = str(settings.db_url)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    database.init_app(app = app)
    
    if settings.allow_auto_generate_tables:
        with app.app_context():
            database.create_all()