from flask import Blueprint, jsonify, request, json, Flask, g
from flask import current_app, Request, Response
import flask
import json

uri = Blueprint("endpoint", __name__, url_prefix="/")

cart=dict()
@uri.route("/healthCheck", methods=["GET"])
def healthCheck():
    return "Working"

# 1st api
@uri.route("/allProducts", methods=["GET"])
def allProducts():
    file=open('products.json')
    data=json.load(file)
    file.close()
    return (jsonify(data),200)

#2nd api
@uri.route("/specificProduct/<int:product_id>", methods=["GET"])
def specificProduct(product_id):
    file=open('products.json')
    data=json.load(file)
    for x in data:
        if x["sku"]==product_id:
            return (jsonify(x),200)
    return ("Product not found",404)

#3rd api
@uri.route("/addProduct/<int:product_id>", methods=["GET"])
def addProduct(product_id):  
    file=open('products.json')
    data=json.load(file)
    for x in data:
        if x["sku"]==product_id:
            if product_id in cart:
                return (jsonify(cart),200)
            else:
                cart[product_id]=x
                return (jsonify(cart),200)
    return ("Product not found",404)

#4th api
@uri.route("/deleteProduct/<int:product_id>", methods=["GET"])
def deleteProduct(product_id):
    if product_id in cart:
        cart.pop(product_id)
        return (jsonify(cart),200)
    else:
        return (jsonify(cart),200)

#5th api
@uri.route("/listCart", methods=["GET"])
def listCart():
    return (jsonify(cart),200)

#6th api
@uri.route("/purchase", methods=["GET"])
def purchase():
    total=0
    for product in cart:
        total=total+cart[product]["price"]
    return (jsonify(total),200)