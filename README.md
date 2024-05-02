------------------------
Name: Jennifer Alcantara 
This README file is for my final project for class IS6011J2-Web Systems Development.
------------------------
The following scripts do as follows:

For this project, A REST API backend for the restaurant 'Dosa' was created. 
We imported and used SQLite3 and FAST API (there are more, but these are the most important modules) in our scripts to initialize a database, query, set rules, and create a web API to make updates to the database/data through the front end as the "client". 

To be installed: sqlite3, FastAPI, and uvicorn in order to begin.

The client/user will have access to create, read, update, or delete from three objects: customers, items, and orders. This will be done on the front end through FAST API (a web API).
We will have the ability to complete these actions with methods: POST, GET, DELETE, and PUT (in the main.py file).

In this repo you will find:
---------------------------
1 json file (example_orders.json) where all of the customers, orders, and items are.
1 db file (db.sqlite) where our SQLite database is. (this is created, if it doesn't exist, when running Init_db.py)
2 scripts, Init_db.py and main.py. 
(The Init_db.py will initialize an empty database using relational constraints (primary keys and foreign keys) from the example_orders.json file. The main.py script is the FastAPI backend that must read and write from db.sqlite.)

In the Init_db.py script,
Lines 3-4, set up the connection to our database: db.sqlite.
Lines 6-39 create the tables and their columns (most importantly their primary and foreign keys).
Lines 41-42 open up the json file that will be used for all the customers, orders, and items.
Lines 44-71 query the database.
Lines 73-74 commit the rules and close the database.

In the main.py script,
Line 7 enables us to use the REST interface to call our functions in our main.py file to implement applications.
Lines 9-69 is where the Customer's methods are applied.
Lines 78-138 is where the Item's methods are applied.
Lines 142-207 is where the Orders methods were applied.

------------------------------------
Final steps to access your fast API:
------------------------------------
First, run your Init_db.py file to create the database file.
Next, run your main.py file and then run the command: "uvicorn main:app --reload". (This runs the live server/application for you.)
Finally, go into your browser (Safari may act funky, use a different web browser) and copy and paste the HTTP link provided upon running the above uvicorn command and then add "/docs" to the end: "http://127.0.0.1:8000/docs"

You'll then be able to complete your actions in a very cool way through your web API: FAST API - Swagger UI!

*----------------------------------------------------*
Thanks Professor !!!
*----------------------------------------------------*
