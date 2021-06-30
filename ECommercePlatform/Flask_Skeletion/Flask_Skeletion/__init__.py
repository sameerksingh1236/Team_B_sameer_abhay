from flask import Flask

from flask_cors import CORS

from .app.controller.controller import uri

import logging

app = Flask(__name__)

# CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(uri)
