import sqlite3, json

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
    timestamp INTEGER,
    notes TEXT,
    cust_id INTEGER,
	FOREIGN KEY(cust_id) REFERENCES customers(id)
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS order_list(
    id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(item_id) REFERENCES items(id)
);
""")

with open ('example_orders.json') as file:
    order_list = json.load(file)

orders = []
customers = {}
items = {}

for order in order_list:
    customers[order["phone"]] = order["name"]
for item in order["items"]:
    items[item["name"]] = item["price"]
        
for phone, name in customers.items():
	cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?)", (name,phone))
     
for name, price in items.items():
     cursor.execute("INSERT INTO items (name, price) VALUES (?, ?)", (name,price))

for order in order_list:
     cursor.execute("SELECT id FROM customers WHERE phone= ?;", (order["phone"],))
     cust_id = cursor.fetchone()[0]
     cursor.execute("INSERT INTO orders (notes, timestamp, cust_id) VALUES (?, ?, ?);",
            (order["notes"], order["timestamp"],cust_id))
     order_id = cursor.lastrowid
     
     for item in order["items"]:
          cursor.execute("SELECT id FROM items WHERE name=?;",(item["name"],))
          item_id = cursor.fetchone()[0]
          cursor.execute("INSERT INTO order_list (order_id, item_id) VALUES (?, ?);",
                (order_id, item_id))

connection.commit()
connection.close()