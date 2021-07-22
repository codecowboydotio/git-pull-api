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
@swag_from('pull.yml')
def pull():
    result_data = request.get_data()
    print(result_data)
    data = request.get_json(force=True)
    print ("\n\n")
    html_url = data['repository']['html_url']
    message = data['commits'][0]['message']
    print (html_url)
    print (message)
    print ("\n\n")
    repo = data['repository']['html_url']
    branch = 'main'
  #  branch = data['branch']
    dest = data['commits'][0]['message']
  #  config_url = data['config_url']
  #  key = data['key']
  #  val = data['val']

    path_exists = Path(dest).is_dir()
    if path_exists == True:
      git_repo = Repo(dest)
      origin = git_repo.remotes.origin 
      origin.pull()
      git_repo.git.reset('--hard')
    else:
      Repo.clone_from(repo, dest)    

    #return jsonify(repo=repo, branch=branch, dest=dest, config_url=config_url, key=key, val=val)
    return jsonify(repo=repo, branch=branch, dest=dest)

@app.route('/info', methods=['GET'])
@swag_from('info.yml')
def info():
    msg = 'This is the API that you see'
    api_ver = '1.0'
    
    return jsonify(status=msg, version=api_ver)

if __name__ == "__main__":
  app.run(host='0.0.0.0')
