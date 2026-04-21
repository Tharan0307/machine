from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from database import get_connection

# Create FastAPI app
app = FastAPI()

# =====================
# CORS — Allow frontend
# to talk to backend
# =====================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# =====================
# Machine Model
# =====================
class Machine(BaseModel):
    machine_name: str
    machine_model: str
    serial_number: str
    location: Optional[str] = None
    status: Optional[str] = "Running"
    ip_address: Optional[str] = None

# =====================
# GET all machines
# =====================
@app.get("/machines")
def get_machines():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM machines")
    machines = cursor.fetchall()
    cursor.close()
    conn.close()
    return machines

# =====================
# GET single machine
# =====================
@app.get("/machines/{machine_id}")
def get_machine(machine_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM machines WHERE id = %s", (machine_id,))
    machine = cursor.fetchone()
    cursor.close()
    conn.close()
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    return machine

# =====================
# POST — Add new machine
# =====================
@app.post("/machines")
def add_machine(machine: Machine):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO machines 
        (machine_name, machine_model, serial_number, location, status, ip_address) 
        VALUES (%s, %s, %s, %s, %s, %s)""",
        (machine.machine_name, machine.machine_model,
         machine.serial_number, machine.location,
         machine.status, machine.ip_address)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Machine added successfully"}

# =====================
# DELETE — Remove machine
# =====================
@app.delete("/machines/{machine_id}")
def delete_machine(machine_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM machines WHERE id = %s", (machine_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Machine deleted successfully"}