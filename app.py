
from flask import Flask
from requests import get
import os

app = Flask('__main__')
SITE_NAME = os.environ.get('PROMETHEUS_URL')
HEADERS = {'Authorization': 'Bearer ' + os.environ.get('TOKEN')}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  return get(SITE_NAME + path, HEADERS, verify=False).content

app.run(host='0.0.0.0', port=8080)
