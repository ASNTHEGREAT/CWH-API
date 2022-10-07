from flask import Flask
from flask_smorest import Api 

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

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

api = Api(app) #connects the flask-smorest extension to the Flask extension

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)