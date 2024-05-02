Name: Jennifer Alcantara This README file is for my final project for class IS6011J2-Web Systems Development.
The following scripts do as follows:

A REST API backend for the restaurant 'Dosa' will be created for this project. We will be importing SQLite3 and fast API into our scripts to initialize a database and then, use a web API to make updates to the database/data on the front end as the client. 

You will need to import sqlite3, FAST API, and uvicorn to begin.

The client/user will have access to create, read, update, or delete three objects: customers, items, and orders, through the web API (fast API).

In this repo you will find:
2 scripts, Init_db.py and main.py.
1 json file (example_orders.json) where all of the customers, orders, and items are.
1 file (db.sqlite) where our SQLite database is.


In the Init_db.py script, 
Lines 3-4, set up the connection to our database: db.sqlite.
Lines 6-39 create the tables and their columns (most importantly their primary and foreign keys).
Lines 41-42 open up the json file that will be used for all the customers, orders, and items.
Lines 44-71 queries the database.
Lines 73-74 commit the rules and close the database.

In the main.py script, 
