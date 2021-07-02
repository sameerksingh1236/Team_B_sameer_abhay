from flask import Blueprint, jsonify, request, json, Flask, g
from flask import current_app, Request, Response
import flask
import json

uri = Blueprint("endpoint", __name__, url_prefix="/")


@uri.route("/healthCheck", methods=["GET"])
def healthCheck():
    return "Working"

#1st api
@uri.route("/allProducts", methods=["GET"])
def allProducts():
    file=open('products.json')
    data=json.load(file)
    return Response(jsonify(data),200)

#2nd api
@uri.route("/specificProduct", methods=["GET"])
def specificProduct():
    file=open('products.json')
    data=json.load(file)
    product_id=request.args['product_id']
    for key,val in data.items():
        if val["sku"]==product_id:
            return Response(jsonify(data[key]),200)
    return Response("Product not found",404)

#3rd api
@uri.route("/addProduct", methods=["GET","POST"])
def allProduct():  
    file=open('products.json')
    data=json.load(file)
    return ""

#4th api
@uri.route("/deleteProduct", methods=["GET"])
def allProducts():
    return "all products instaed of this"

#5th api
@uri.route("/listCart", methods=["GET"])
def allProducts():
    return "all products in cart"

#6th api
@uri.route("/purchase", methods=["GET"])
def allProducts():
    return "list product in current cart"
