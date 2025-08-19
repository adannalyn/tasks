from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr

app = FastAPI()


contacts_db = {}


class Contact(BaseModel):
    name: str
    phone: str
    email: EmailStr


@app.post("/contacts")
def create_contact(contact: Contact):
    try:
        if contact.name in contacts_db:
            raise HTTPException(
                status_code=400, detail="Contact already exists")
        contacts_db[contact.name] = {
            "phone": contact.phone,
            "email": contact.email
        }
        return {
            "message": f"Contact '{contact.name}' created successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/contacts")
def get_contact(
        name: str = Query(..., description="Name of the contact to search")):
    try:
        if name not in contacts_db:
            raise HTTPException(status_code=404, detail="Contact not found")
        return {
            "name": name, **contacts_db[name]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/contacts/{name}")
def update_contact(name: str, phone: str = None, email: EmailStr = None):
    try:
        if name not in contacts_db:
            raise HTTPException(status_code=404, detail="Contact not found")
        if phone:
            contacts_db[name]["phone"] = phone
        if email:
            contacts_db[name]["email"] = email
        return {
            "message": f"Contact '{name}' updated successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/contacts/{name}")
def delete_contact(name: str):
    try:
        if name not in contacts_db:
            raise HTTPException(
                status_code=404, detail="Contact not found")
        del contacts_db[name]
        return {
            "message": f"Contact '{name}' deleted successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
