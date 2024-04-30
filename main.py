from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Customer(BaseModel):
      cust_id: int | None = None
      name: str
      phone: int

@app.post("/customers/")
def create_customer(customer: Customer):
    if customer.cust_id != None:
        raise HTTPException(status_code=400, detail="cust_id can't be set on post request")
    
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO customers WHERE (name, phone) VALUES (?, ?);",(customer.name, customer.phone))
    customer.cust_id = cursor.lastrowid
    connection.commit()
    connection.close()

    return customer

@app.get("/customers/{cust_id}")
def read_customer(cust_id: int, q=None):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM customers WHERE phone= ?", (cust_id,))
    customer = cursor.fetchone()
    connection.close()

    if customer != None:
            return Customer (cust_id=customer[0], name=customer[1], phone=customer[2])       
    else:
         raise HTTPException(status_code=404, detail="Item not found")
    
@app.put("/customers/{cust_id}")
def update_customer(cust_id: int, customer: Customer):
    if customer.cust_id != None and customer.cust_id != cust_id:
        raise HTTPException(status_code=404, detail="Customer ID doesn't match ID in Path")
    
    customer.cust_id = cust_id
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("UPDATE customers SET name=?, phone=? WHERE id=?;", (customer.name, customer.phone, cust_id))
    total_changes = connection.total_changes
    connection.commit()
    connection.close()

    if total_changes == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return customer

@app.delete("/customers/{cust_id}")
def delete_customer(cust_id: int):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM customers WHERE id=? ", (cust_id))
    total_changes = connection.total_changes
    connection.commit()
    connection.close()

    if total_changes != 1:
        raise HTTPException(status_code=400, detail="{total_changes} rows were affected")
    return total_changes

#### Items, Orders, and Order List Next

    #update_customer_encoded = jsonable_encoder(customer)
    #customer[cust_id] = update_customer_encoded

    #return update_customer_encoded

