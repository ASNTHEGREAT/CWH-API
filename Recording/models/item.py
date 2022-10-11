from enum import unique
from db import db

class ItemModel(db.Model):  #This now becomes a mapping between a row and a table to a python class and therefore python objects.
    __tablename__ = "items" #Tells SQLAlchemy that we want to create or use a table called "items" for all the objects of this class.

    id = db.Column(db.Integer, primary_key=True)    #Define a Column which is going to be a part of the "items" table, we specify that is going to be an integer column and that it(column) is the primary key of the table. 
    name = db.Column(db.String(80), unique=True, nullable=False) #Define a new Column 'name' which will hold names and the max length of the characters is 80, name of the item is going to be unique, and you cannot create an item that doesn't have a name.
    price = db.Column(db.Float(precision=2), unique=False, nullabe=False) #Define a new Column 'price' which will hold Float value upto 2 places after the radix, and multiple items can have the same price but it cannot be NULL.
    store_id = db.Column(db.Integer, db.Foreign_key("stores.id"), unique=False, nullable=False) #The value that will be stored inside this column has to match the value of id that we define in the stores table, basically it is mapped to stores table using a foreign key.
    store = db.relationship("StoreModel", back_populates="items") #links this item to 'StoreModel' class in Store.py
