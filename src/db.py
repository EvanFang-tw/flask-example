from flask_sqlalchemy import SQLAlchemy
import configparser


db = SQLAlchemy()


def get_db_url():
    config = configparser.ConfigParser()
    config.read("configs/db.ini")

    psql = config["postgresql"]
    username = psql["username"]
    password = psql["password"]
    host = psql["host"]
    port = psql["port"]
    database = psql["database"]

    return f"postgresql://{username}:{password}@{host}:{port}/{database}"
