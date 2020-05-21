from flask import Flask
from flask_restful import Resource, Api
from src.hotel import Hoteis, Hotel

app = Flask(__name__)
api = Api(app)

api.add_resource(Hoteis,'/hoteis')
api.add_resource(Hotel,'/hoteis/<int:id>')
if __name__ == '__main__':
    app.run(debug=True)