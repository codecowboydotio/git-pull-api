#!/usr/bin/python

import requests

def test_pull_api():
  response = requests.post('http://127.0.0.1:81/pull')
  assert response.status_code == 200
  assert response.headers["Content-Type"] == "application/json"

def test_docs():
  response = requests.get('http://127.0.0.1:81/apidocs')
  assert response.status_code == 200

def test_root():
  response = requests.get('http://127.0.0.1:81/')
  assert response.status_code == 200
