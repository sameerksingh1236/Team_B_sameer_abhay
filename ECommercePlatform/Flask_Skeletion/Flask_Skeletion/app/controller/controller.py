from flask import Blueprint, jsonify, request, json, Flask, g
from flask import current_app
import flask


uri = Blueprint("endpoint", __name__, url_prefix="/")


@uri.route("/healthCheck", methods=["GET"])
def healthCheck():
    return "Working"
