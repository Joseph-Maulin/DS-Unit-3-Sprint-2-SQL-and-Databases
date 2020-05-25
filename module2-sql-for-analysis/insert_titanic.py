import psycopg2
from psycopg2.extras import DictCursor, execute_values
from dotenv import load_dotenv
import pandas as pd
import os
import json


load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="DB_NAME")
DB_USER = os.getenv("DB_USER", default="DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", default="DB_HOST")

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)


df = pd.read_csv('titanic.csv')



def insert_df(conn, sql):
    cur = conn.cursor(cursor_factory=DictCursor)

    try:
        cur.execute(sql)
        conn.commit()
        print('row added')
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        cur.close()


def import_data():
    cur = conn.cursor(cursor_factory=DictCursor)

    try:
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS titanic(
                        idx SERIAL PRIMARY KEY,
                        Survived int,
                        Pclass int,
                        Name VARCHAR(100),
                        Sex VARCHAR(10),
                        Age int,
                        Siblings_Spouses_Aboard int,
                        Parents_Children_Aboard int,
                        Fare FLOAT
                    );
                    """
                    )

        conn.commit()

    except Exception as e:
        print(e)

    for i in df.index:

        name = df.loc[i]['Name'].replace("'", "''")

        table_values = [x for x in df.loc[i].values]
        values = tuple([x for x in table_values[:2]] + [name] + [x for x in table_values[3:]])

        print(f"row {i}")

        sql = """
                INSERT INTO titanic(Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
                VALUES (%s, %s, '%s', '%s', %s, %s, %s, %s)
                """ % values

        insert_df(conn, sql)

    print("data imported..")


if __name__ == '__main__':
    cur = conn.cursor(cursor_factory=DictCursor)

    cur.execute("""
                SELECT AVG(age) AS AVG_AGE
                FROM titanic;
    """)

    print(dict(cur.fetchall()[0]))
