import string
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Customer(BaseModel):
      cust_id: int | None = None
      name: str
      phone: int

@app.post("/customers/{cust_id}")
def create_customer(customer: Customer):
    if customer.cust_id != None:
        raise HTTPException(status_code=400, detail="cust_id can't be set on post request")
    
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?);", (customer.name, customer.phone))
    customer.cust_id = cursor.lastrowid
    connection.commit()
    connection.close()

    return customer

@app.get("/customers/{cust_id}")
def read_customer(cust_id: int, customer: Customer):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM customers WHERE name=?, phone=?", (cust_id,))
    customer = cursor.fetchone()
    connection.close()

    if customer.cust_id != None:
        return Customer (cust_id=customer[0], name=customer[1], phone=customer[2])       
    else:
        raise HTTPException(status_code=404, detail="Customer not found")
    
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


#####
##### Items
#####

class Item(BaseModel):
      item_id: int | None = None
      name: str
      price: int

@app.post("/items/")
def create_item(item: Item):
    if item.item_id != None:
        raise HTTPException(status_code=400, detail="item_id can't be set on post request")
    
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO items (name, price) VALUES (?, ?);",(item.name, item.price))
    item.item_id = cursor.lastrowid
    connection.commit()
    connection.close()

    return item

@app.get("/items/{item_id}")
def read_item(item_id: int, q=None):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM items WHERE price= ?", (item_id,))
    item = cursor.fetchone()
    connection.close()

    if item != q:
            return Item (item_id=item[0], name=item[1], price=item[2])       
    else:
         raise HTTPException(status_code=404, detail="Item not found")
    
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item.item_id != None and item.item_id != item_id:
        raise HTTPException(status_code=404, detail="Item ID doesn't match ID in Path")
    
    item.item_id = item_id
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("UPDATE items SET name=?, price=? WHERE id=?;", (item.name, item.price, item_id))
    total_changes = connection.total_changes
    connection.commit()
    connection.close()

    if total_changes == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM items WHERE id=? ", (item_id))
    total_changes = connection.total_changes
    connection.commit()
    connection.close()

    if total_changes != 1:
        raise HTTPException(status_code=400, detail="{total_changes} rows were affected")
    return total_changes

#####
#####Orders
#####

class Order(BaseModel):
    order_id: int | None = None
   #cust_id: int | None = None
    timestamp: int
    notes: str

@app.post("/orders/")
def create_order(order_id: int, order: Order):
    if order.order_id != None:
        raise HTTPException(status_code=400, detail="order_id can't be set on post request")
    #if order.cust_id != None :
        #raise HTTPException(status_code=400, detail="cust_id can't be set on post request")
    
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO orders (order_id, timestamp, notes) VALUES (?, ?, ?);",(order.order_id, order.timestamp, order.notes,))
    order.order_id = cursor.lastrowid
    connection.commit()
    connection.close()

    return order

@app.get("/orders/{order_id}")
def read_order(order_id: int, order: Order):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM orders WHERE order_id= ?", (order_id))
    order = cursor.fetchone()
    connection.close()

    if order != None:
            return Order (order_id=order[0], timestamp=order[1], notes=order[2])       
    else:
         raise HTTPException(status_code=404, detail="Order not found")

@app.put("/orders/{order_id}")
def update_order(order_id: int, order: Order):
    if order.order_id != None and order.order_id != order_id:
        raise HTTPException(status_code=404, detail="Order ID doesn't match ID in Path")
    
    order.order_id = order_id
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("UPDATE orders SET timestamp=?, notes=? WHERE id=?;", (order.timestamp, order.notes, order_id,))
    total_changes = connection.total_changes
    connection.commit()
    connection.close()

    if total_changes == 0:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM orders WHERE id=? ", (order_id))
    total_changes = connection.total_changes
    connection.commit()
    connection.close()

    if total_changes != 1:
        raise HTTPException(status_code=400, detail="{total_changes} rows were affected")
    return total_changes
