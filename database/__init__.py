from flask_sqlalchemy import SQLAlchemy

engine_options: dict = {
    "pool_size": 100,
    "echo_pool": True,
    "pool_pre_ping": True
}

db = SQLAlchemy(engine_options=engine_options)


def reset_database():
    db.drop_all()
    db.create_all()
