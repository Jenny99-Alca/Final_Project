Name: Jennifer Alcantara This README file is for my final project for class IS6011J2-Web Systems Development.
The following scripts do as follows:

For this project, A REST API backend for the restaurant 'Dosa' was created. We imported SQLite3 and fast API into our scripts to initialize a database and then, used a web API to make updates to the database/data on the front end as the client. 

To be imported: sqlite3, FAST API, and uvicorn in order to begin.

The client/user will have access to create, read, update, or delete from three objects: customers, items, and orders. This will be done on the front end through FAST API (a web API).

In this repo you will find:
1 json file (example_orders.json) where all of the customers, orders, and items are.
1 db file (db.sqlite) where our SQLite database is. (this is created, if it doesn't exist, when running Init_db.py)
2 scripts, Init_db.py and main.py. 
(The Init_db.py will initialize an empty database using relational constraints (primary keys and foreign keys) from the example_orders.json file. The main.py script is the FastAPI backend that must read and write from db.sqlite.)


In the Init_db.py script, 
Lines 3-4, set up the connection to our database: db.sqlite.
Lines 6-39 create the tables and their columns (most importantly their primary and foreign keys).
Lines 41-42 open up the json file that will be used for all the customers, orders, and items.
Lines 44-71 queries the database.
Lines 73-74 commit the rules and close the database.

In the main.py script,
