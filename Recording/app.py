from email import message
from flask import Flask, request
from db import stores, items
from flask_smorest import abort
import uuid

app = Flask(__name__)

@app.get("/")
def greeter():
    return '''Hello Everyone, to checkout the api try searching for "http://127.0.0.1:5000/store" or "http://127.0.0.1:5000/item"'''


@app.get("/store")  # http://127.0.0.1:5000/store
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found.")


@app.post("/store/<string:name>/item")
def create_item(name):
    item_data = request.get_json()
    if(
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(
            400,
            message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON paylaod."
        )
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found.")
    
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item


@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found.")

