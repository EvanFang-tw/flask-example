from flask_sqlalchemy import SQLAlchemy
import configparser
import os
from utils import get_file_dir


db = SQLAlchemy()


def get_db_url():
    config = configparser.ConfigParser()
    config.read(os.path.join(get_file_dir(__file__), "db.ini"))

    psql = config["postgresql"]
    username = psql["username"]
    password = psql["password"]
    host = psql["host"]
    port = psql["port"]
    database = psql["database"]

    return f"postgresql://{username}:{password}@{host}:{port}/{database}"
