from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic") #Links it to 'ItemModel' class in item.py, lazy=dynamic means that the items here will not be fetched from the database until we tell it to.

    
