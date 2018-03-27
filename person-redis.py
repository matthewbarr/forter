#!/usr/local/bin/python
from flask import Flask, request, jsonify
import redis 
import uuid

db = redis.Redis('redis')


app = Flask(__name__)

@app.route("/person/", methods=["POST"])
def add_name():
    req_data = request.get_json()
    name = req_data['name']
    id = {'_id': uuid.uuid4()}

    db.set(id['_id'], name)
    return jsonify(id), 201


@app.route("/person/<uuid:id>", methods=["GET"])
def retrieve(id):
    name = {'name': db.get(id)}
    return jsonify(name),200
    


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
