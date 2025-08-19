from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float


products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Headphone", "price": 149.49},
    {"id": 3, "name": "Keyboard", "price": 29.99},
]
