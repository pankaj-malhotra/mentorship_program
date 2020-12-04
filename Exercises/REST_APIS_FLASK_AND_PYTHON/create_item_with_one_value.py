#Program to add an item with a single value (Key, Value)

from flask import Flask, request
from flask_restful import Resource, Api
from redis import Redis

app = Flask(__name__)
api = Api(app)
r = Redis(host='localhost', port=6379, db=0)

items = []

class Item(Resource):
    def get(self, name):
        result = r.get(name)

        if result:
            return {'name': name, 'price': result.decode("utf-8")}
        else:
            return {'item': None}, 404

    def post(self, name):
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        r.set(name, data['price'])
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
