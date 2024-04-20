import sqlite3 

connection = sqlite3.connect("db.sqlite")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
	id INTEGER PRIMARY KEY,
	name CHAR(64) NOT NULL,
	phone CHAR(10) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS items(
	id INTEGER PRIMARY KEY,
	name CHAR(64) NOT NULL,
	price REAL NOT NULL
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
	id INTEGER PRIMARY KEY,
	FOREIGN KEY(cust_id) REFERENCES customers(id),
    notes TEXT
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS order_list(
    id INTEGER PRIMARY KEY,
    order_id INTIGER NOT NULL,
    item_id INTEGER NOT NULL,
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(cust_id) REFERENCES customers(id)
);
""")
connection.commit()
connection.close()