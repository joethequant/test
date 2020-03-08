# app.py - a minimal flask api using flask_restful
# https://medium.com/bitcraft/docker-composing-a-python-3-flask-app-line-by-line-93b721105777

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
#api = Api(app)

@app.route('/')
def hello_world():
    return 'Hey world! I am deeply in love with Christina R!!!!!'

@app.route('/joe')
def hello_joe():
    return 'Hello, Joe!'

# class HelloWorld(Resource):
#     def get(self):
#         return {'Joe': 'world'}

# api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    