from flask import Flask
from flask_cors import CORS

from flask import Flask
from .controller.controller import uri

app = Flask(__name__)
CORS(app)
app.register_blueprint(uri)
