from flask import Flask
from db import init_database

def register_startup_event(app: Flask):
    """
    Actions to be performed on Application Startup
    """
    init_database(app)
    