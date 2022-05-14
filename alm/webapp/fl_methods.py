from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def hello_world():
    return 'request.method is ' + request.method

@app.route('/login', methods=['POST'])
def login():

    return 'Success!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')