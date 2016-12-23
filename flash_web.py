from flask import Flask
import json
import redis
from flask import render_template

app = Flask(__name__)

@app.route('/')
def getData():
    return "hell world"

if __name__ == '__main__':
    app.run(host='127.0.0.1')
