#!/usr/bin/python
from flask import Flask, jsonify, request, redirect
from flasgger import Swagger
from flasgger.utils import swag_from, validate
from jsonschema import ValidationError

app = Flask(__name__)
swagger = Swagger(app)

@app.route ('/')
def root():
    return redirect("/apidocs", code=302)
@app.route('/pull', methods=['POST'])
@swag_from('unit-flask-git.yml')
def pull():
    repo = request.args.get('repo')
    branch = request.args.get('branch')
    dest = request.args.get('dest')

    return jsonify(repo=repo, branch=branch, dest=dest)

app.run(host='0.0.0.0', debug=True, port=81)
