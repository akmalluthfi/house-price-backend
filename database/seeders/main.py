import os
from sqlalchemy import text
from app.core.db import engine

BASE_DIR = os.path.dirname(__file__)


def seed():
    with engine.connect() as conn:
        with open(os.path.join(BASE_DIR, "locations.sql"), "r") as file:
            sql_statements = file.read()
            try:
                conn.execute(text(sql_statements))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()

        with open(os.path.join(BASE_DIR, "houses.sql"), "r") as file:
            sql_statements = file.read()
            try:
                conn.execute(text(sql_statements))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()


if __name__ == "__main__":
    print("SQL seeding started.")
    seed()
    print("SQL seeding completed.")
