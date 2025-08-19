import os
from products import products
import json
import math


FILE_PATH = "cart.json"


def load_goods():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}


def save_goods(products):
    with open(FILE_PATH, "w") as file:
        json.dump(products, file, indent=4)


def calculate_subtotal(product):
    subtotal = 0.0
    for product_id_string, qty in product.items():
        product_id_int = int(product_id_string)
        for product in products:
            if product["id"] == product_id_int:
                subtotal += product["price"] * qty
                break
    return math.floor(math.fsum([subtotal]))


def add_to_cart(product_id: int, qty: int):
    product_list = load_goods()
    for product in products:
        if product["id"] == product_id:
            if qty <= 0:
                return {
                    "error": "Quantity must be positive"
                }
            product_key = str(product_id)
            if product_key in product_list:
                product_list[product_key] += qty
            else:
                product_list[product_key] = qty
            save_goods(product_list)
            subtotal = calculate_subtotal(product_list)
            return {
                "message": f"Added {qty} x {product['name']} to cart",
                "product": product,
                "qty": product_list[product_key],
                "cart_subtotal": subtotal
            }
    return {
        "message": "Product not found"
    }


def view_cart():
    product_list = load_goods()
    if not product_list:
        return {
            "message": "Cart is empty"
        }
    items = []
    for product_id_string, qty in product_list.items():
        product_id = int(product_id_string)
        for product in products:
            if product["id"] == product_id:
                items.append({
                    "id": product["id"],
                    "name": product["name"],
                    "unit_price": product["price"],
                    "quantity": qty,
                    "total_price": round(product["price"] * qty, 2)
                })
                break
    return {
        "items": items,
        "cart_subtotal": calculate_subtotal(product_list)
    }


def checkout():
    product_list = load_goods()
    if not product_list:
        return {
            "message": "Cart is empty"
        }
    total = calculate_subtotal(product_list)
    save_goods({})
    return {
        "message": "Checkout successful", "total": total
    }
