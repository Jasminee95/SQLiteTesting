import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS stores 
    (store_id INTEGER PRIMARY KEY, location TEXT)
"""

cursor.execute(command1)

command2 = """CREATE TABLE IF NOT EXISTS purcheses
    (purcheses_id INTEGER PRIMARY KEY, 
    store_id INTEGER, total_cost FLOAT, FOREIGN KEY(store_id) REFERENCES stores(store_id) 
)"""

cursor.execute(command2)

cursor.execute("INSERT INTO stores VALUES (21, 'Minneapolis, MN')")
cursor.execute("INSERT INTO stores VALUES (95, 'Chicago, IL')")
cursor.execute("INSERT INTO stores VALUES (64, 'Iowa City, IA')")

cursor.execute("INSERT INTO purcheses VALUES (54, 21, 15.49)")
cursor.execute("INSERT INTO purcheses VALUES (23, 64, 21.12)")

connection.commit()

cursor.execute("SELECT * FROM purcheses")

reults = cursor.fetchall()
print(reults)

