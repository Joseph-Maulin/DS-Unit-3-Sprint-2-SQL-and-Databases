import psycopg2
from dotenv import load_dotenv
import os


load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="DB_NAME")
DB_USER = os.getenv("DB_USER", default="DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", default="DB_HOST")

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)



cur = conn.cursor()

cur.execute('SELECT * from test_table;')


for row in cur.fetchall():
    print(row)
