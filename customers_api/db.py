from flask_sqlalchemy import SQLAlchemy
from os import environ
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
dotenv_path = '../.env'
load_dotenv(dotenv_path)

db = SQLAlchemy()

class DbConfig:
    def __init__(self):
        self.DB_USERNAME = environ.get('DB_USERNAME')
        self.DB_PASSWORD = environ.get('DB_PASSWORD')
        self.DB_HOST = environ.get('DB_HOST')
        self.DB_PORT = int(environ.get('DB_PORT'))
        self.DB_NAME = environ.get('DB_NAME')

    def getUri(self):
        return "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(self.DB_USERNAME, self.DB_PASSWORD, self.DB_HOST,
                                                              self.DB_PORT, self.DB_NAME)
