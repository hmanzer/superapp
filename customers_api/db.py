from flask_sqlalchemy import SQLAlchemy
from os import environ
# from dotenv import load_dotenv, find_dotenv
# from pathlib import Path


# load_dotenv()
# env_path = os.path.abspath('..') + '.env'
# print(env_path)
#load_dotenv(find_dotenv())


db = SQLAlchemy()

class DbConfig:
    def __init__(self):
        self.DB_USERNAME = environ.get('MYSQL_USER')
        self.DB_PASSWORD = environ.get('MYSQL_PASSWORD')
        self.DB_HOST = environ.get('DB_HOST')
        self.DB_PORT = int(environ.get('DB_PORT'))
        self.DB_NAME = environ.get('DB_NAME')

    def getUri(self):
        return "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(self.DB_USERNAME, self.DB_PASSWORD, self.DB_HOST,
                                                              self.DB_PORT, self.DB_NAME)
