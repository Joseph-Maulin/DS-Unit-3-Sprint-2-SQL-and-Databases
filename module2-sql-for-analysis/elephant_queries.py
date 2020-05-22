import psycopg2
from psycopg2.extras import DictCursor, execute_values
from dotenv import load_dotenv
import os
import json


load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="DB_NAME")
DB_USER = os.getenv("DB_USER", default="DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", default="DB_HOST")

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)



cur = conn.cursor(cursor_factory=DictCursor)



cur.execute('SELECT * from test_table;')


for row in cur.fetchall():
    print(row)


my_dict = {"hello":2}

insertion_query = "INSERT INTO test_table (name, data) VALUES %s"
execute_values(cur, insertion_query, [
("Test1", json.dumps(my_dict)),
("Test2", 'null')
])

conn.commit()

cur.execute('SELECT * from test_table;')


for row in cur.fetchall():
    print(row)

cur.close()
conn.close()
