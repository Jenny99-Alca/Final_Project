from fastapi import FastAPI, HTTPException, sqlite3

app = FastAPI()

customers = [
    (0, "609-555-0124", "Karl"),
    (1, "609-555-1234", "Mike"),
    (3, "609-555-4302", "Ryan"),
]

@app.get("/customers/{cust_id}")
def read_item(cust_id: int, q=None):
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM customers WHERE phone= ?", (cust_id,))
    customer = cursor.fetchone()
    connection.close()

    if customer != None:
            return {
                "id": customer[0], 
                "name": customer[1],
                "phone": customer[2]
            }
    raise HTTPException(status_code=404, detail="Item not found")