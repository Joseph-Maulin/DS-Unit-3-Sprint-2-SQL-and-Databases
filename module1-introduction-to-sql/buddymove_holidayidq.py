import os
import sqlite3
import pandas as pd


df = pd.read_csv("buddymove_holidayiq.csv")


print(f"Shape: {df.shape}")
print(df.isnull().sum())
print(df.head())


connection = sqlite3.connect("buddymove_holidayiq.sqlite3")
cursor = connection.cursor()


df.to_sql('review', connection, index=False, if_exists='replace')


cursor.execute("""SELECT * FROM review;""")

for row in cursor.fetchall():
    print(row)
print("\n")

cursor.execute("""SELECT COUNT(*)
             FROM review""")
print(f"Count total users: {cursor.fetchall()[0][0]}\n")


cursor.execute("""
            SELECT COUNT(*)
            FROM review
            WHERE Nature>=100 and Shopping>=100;
        """)

print(f"Count Nature and Shopping >=100: {cursor.fetchall()[0][0]}\n")


cursor.execute("""
            SELECT
                AVG(Sports) as Sports_AVG
                ,AVG(Religious) as Religious_AVG
                ,AVG(Nature) as Nature_AVG
                ,AVG(Theatre) as Theatre_AVG
                ,AVG(Shopping) as Shopping_AVG
                ,AVG(Picnic) as Picnic_AVG
            FROM review;
""")


for row in cursor.fetchall():
    print(row)
print("\n")



connection.close()
