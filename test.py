import redis
import json
from flask import Flask

app = Flask(__name__)

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

