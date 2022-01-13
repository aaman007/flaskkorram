from flask import Flask
from flask_smorest import Api

from .settings import INSTALLED_BLUEPRINTS
from ..utils import register_blueprints


app = Flask(__name__)
app.config["API_TITLE"] = "Books API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"

api = Api(app)

register_blueprints(api, INSTALLED_BLUEPRINTS)


@app.route('/')
def home():
    return 'Welcome to bookly'