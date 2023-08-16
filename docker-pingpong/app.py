from flask import Flask, Response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET'])
def ping():

    response = Response(response='pong', status=200, mimetype='text/plain')


    return response 

if __name__ == '__main__':
    app.run()
