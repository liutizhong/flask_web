from flask import Flask, render_template, request, redirect
import redis
import json
from app import app

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index1.html')

@app.route('/getData')
def getData():
    hashkey = "pc::key"
    try:
        if (hashkey == ""):
            hashkey = "pc::key"
        r = redis.StrictRedis(host='10.10.10.122', port='6379', db=1);
        values = r.hgetall(hashkey)
        arr = []
        for key in values:
            arr.append([key, values[key]])
            print key,"000" ,  values[key]
        return json.dumps(arr)
    except Exception, exception:
        print exception


if __name__ == '__main__':
  app.run(port=33507)