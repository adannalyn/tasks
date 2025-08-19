from fastapi import FastAPI, Query
from cart import add_to_cart, view_cart, checkout
from products import products

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {
        "message": "KodeCamp Online Mart"
    }


@app.get("/products")
async def view_items():
    return products


@app.post("/cart/add")
def add_cart_item(
        product_id: int = Query(..., description="Product ID"),
        qty: int = Query(..., description="Quantity needed")):
    return add_to_cart(product_id, qty)


@app.get("/cart")
def ger_cart():
    return view_cart()


@app.get("/cart/checkout")
def cart_checkout():
    return checkout()
