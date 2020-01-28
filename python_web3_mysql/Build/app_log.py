from flask import Flask
from flask import Response
from flask import request
from redis import Redis
from datetime import datetime
import MySQLdb
import sys
import redis 
import time
import hashlib
import os
import json

app = Flask(__name__)
startTime = datetime.now()


MYSQL_HOST=os.environ['MYSQL_HOST']
MYSQL_PORT=os.environ['MYSQL_PORT']
MYSQL_USER_ID=os.environ['MYSQL_USER_ID']
MYSQL_USER_PASSWORD=os.environ['MYSQL_USER_PASSWORD']
print("MYSQL_HOST:",MYSQL_HOST)
print("MYSQL_USER_ID:",MYSQL_USER_ID)
print("MYSQL_USER_PASSWORD:",MYSQL_USER_PASSWORD)
#db = MySQLdb.connect("mysql","root","password1234")
#db = MySQLdb.connect("10.97.147.147:3306","root","password1234")
#db = MySQLdb.connect("10.97.147.147","root","password1234")
db = MySQLdb.connect(MYSQL_HOST,MYSQL_USER_ID,MYSQL_USER_PASSWORD)
cursor = db.cursor()

@app.route('/init')
def init():
    cursor.execute("DROP DATABASE IF EXISTS LOGDB")
    cursor.execute("CREATE DATABASE LOGDB")
    cursor.execute("USE LOGDB")
    sql = """CREATE TABLE systemlog (
         ID int,
         eventtime timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
         MESSAGE varchar(100)
     )"""
    cursor.execute(sql)
    db.commit()
    return "DB Init done" 

@app.route("/systemlog/add", methods=['POST'])
def add_systemlog():
    req_json = request.get_json()   
    print((req_json['id'], req_json['message']))

    cursor.execute("INSERT INTO logdb.systemlog(ID, MESSAGE) VALUES (%i,%s)", (req_json['id'], req_json['message']))
    db.commit()
    return Response("Added", status=200, mimetype='application/json')

@app.route('/systemlog/<id>')
def get_systemlog(id):
    hash = hashlib.sha224(str(id)).hexdigest()
    if True:
        cursor.execute("select id, eventtime, message from logdb.systemlog where ID=" + str(id))
        data = cursor.fetchone()
        if data:
            result = {"id": 0,"eventtime":startTime,"message": ""}
            print(data[0])
            print(data[1])
            print(data[2])


            result["id"] = data[0]
            result["eventtime"] = data[1]
            result["message"] = data[2]
            return result
        else:
            return "Record not found"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
