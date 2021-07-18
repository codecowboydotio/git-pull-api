#!/usr/bin/python
from flask import Flask, jsonify, request, redirect
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route ('/')
def root():
    return redirect("/apidocs", code=302)
@app.route('/pull', methods=['POST'])
def pull():
    """Example git pull API for unit (works outside of unit actually).
    Pull API to retrieve git repo ready to use on the system that the API runs on.
    ---
    parameters:
      - name: repo
        in: query
        type: string
        required: false
      - name: branch
        in: query
        type: string
        required: false
      - name: dest
        in: query
        type: string
        required: false
    responses:
      500:
        description: Something went very wrong
      200:
        description: Return the repo, branch and destination
        schema:
          properties:
            repo:
              type: string
              description: The Repository
              default: none
            branch:
              type: string
              description: The Branch
              default: none
            dest:
              type: string
              description: The Destination
              default: none
    """
    repo = request.args.get('repo')
    branch = request.args.get('branch')
    dest = request.args.get('dest')

    return jsonify(repo=repo, branch=branch, dest=dest)

app.run(host='0.0.0.0', debug=True, port=81)
