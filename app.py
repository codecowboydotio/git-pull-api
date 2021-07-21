from flask import Flask, jsonify, request, redirect
from flasgger import Swagger
from flasgger.utils import swag_from, validate
from jsonschema import ValidationError
import git
from git import Repo
from pathlib import Path

app = Flask(__name__)
swagger = Swagger(app)

@app.route ('/')
def root():
    return redirect("/apidocs", code=302)
@app.route('/pull', methods=['POST'])
@swag_from('unit-flask-git.yml')
def pull():
    result_data = request.get_data()
    print(result_data)
    data = request.get_json(force=True)
    repo = data['repo']
    branch = data['branch']
    dest = data['dest']

    path_exists = Path(dest).is_dir()
    if path_exists == True:
      git_repo = Repo(dest)
      origin = git_repo.remotes.origin 
      origin.pull()
      git_repo.git.reset('--hard')
    else:
      Repo.clone_from(repo, dest)    

    return jsonify(repo=repo, branch=branch, dest=dest)

if __name__ == "__main__":
  app.run(host='0.0.0.0')
