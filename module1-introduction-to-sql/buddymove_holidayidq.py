import os
import sqlite3
import pandas as pd


df = pd.read_csv("buddymove_holidayiq.csv")


print(f"Shape: {df.shape}")
print(df.isnull().sum())
print(df.head())


connection = sqlite3.connect("buddymove_holidayiq.sqlite3")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


df.to_sql('review', connection, index=False, if_exists='replace')


cursor.execute("""SELECT * FROM review LIMIT 5;""")

for row in cursor.fetchall():
    print(dict(row))
print("\n")


cursor.execute("""SELECT COUNT(*) AS USERS
             FROM review""")

print(dict(cursor.fetchall()[0]))
print("\n")


cursor.execute("""
            SELECT COUNT(*) AS Nature_And_Shoppers_Over_100
            FROM review
            WHERE Nature>=100 and Shopping>=100;
        """)

print(dict(cursor.fetchall()[0]))
print("\n")


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
