import redis
import json
from flask import Flask
app = Flask(__name__)

class DBConnect:

    def __init__(self):
        self.host ="10.10.10.122";
        self.port ="6379";
        self.database="1";


    def write(self,website,city,year,month,day,deal_number):
        try:
            key = '_'.join([website,city,str(year),str(month),str(day)])
            val = deal_number;
            r = redis.StrictRedis(host=self.host,port=self.port,db=self.database);
            r.set(key,val);
        except Exception, exception:
            print exception;

    def read(self,website,city,year,month,day):
        try:
            key = '_'.join([website,city,str(year),str(month),str(day)]);
            r = redis.StrictRedis(host=self.host,port=self.port,db=self.database);
            value = r.get(key);
            print value;
            return value;
        except Exception, exception:
            print exception;

    @app.route('/data')
    def getData(self):
        hashkey="pc::key"
        try:
            if(hashkey==""):
                hashkey="pc::key"
            r= redis.StrictRedis(host=self.host,port=self.port,db=self.database);
            values=r.hgetall(hashkey)
            arr = []
            for key in values :
                arr.append([key,values[key]])
            return json.dumps(arr)
        except Exception, exception:
            print exception


if __name__ == '__main__':
     db =DBConnect()
     db.write('meituan','beijing',2013,9,1,8000);
     db.read('meituan','beijing',2013,9,1);
     db.getData()



