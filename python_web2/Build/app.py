from flask import Flask
from datetime import datetime
import socket
app = Flask(__name__)
@app.route("/")

def hello():
    hostname = socket.gethostname()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    result = "hostname:" + hostname + " Current time:" + date_time + "\n"
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
