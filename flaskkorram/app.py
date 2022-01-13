from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from .bookly.app import app as bookly_app
from .productly.app import app as productly_app


app = Flask(__name__)

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/bookly': bookly_app,
    '/productly': productly_app
})

@app.route('/')
def hello():
    return 'Welcome to Home Page'


