from app import app
from flask import request,make_response,jsonify
from APIs.central_node import *
from urllib.parse import urlparse,parse_qs


@app.route('/', methods=['GET'])
def index():
    return jsonify({"Message":"Welcome to the Place's search API!"})

@app.route('/search',methods=['GET'])
def search_place():
    data = request.args.to_dict()
    response = getData(data)

    return response