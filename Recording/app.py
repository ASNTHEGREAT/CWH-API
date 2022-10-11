import os

from flask import Flask
from flask_smorest import Api 

from db import db
import models

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

def create_app(db_url=None):
    app = Flask(__name__)

    @app.get("/")
    def greeter():
        return "Hello Everyone, to checkout the api try searching for 'http://127.0.0.1:5000/store' or 'http://127.0.0.1:5000/item'"

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdeliver/net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URL"] = db_url or   os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app) #connects the flask-smorest extension to the Flask extension

    with app.app_context():
        db.create_all() #This will create all our tables and if the already exist this will not be executed.

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)

    return app