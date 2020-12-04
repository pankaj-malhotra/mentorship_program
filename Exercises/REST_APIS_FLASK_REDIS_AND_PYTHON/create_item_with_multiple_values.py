#Program to add an item with multiple values

from flask import Flask, request
from flask_restful import Resource, Api
from redis import Redis

app = Flask(__name__)
api = Api(app)
r = Redis(host='localhost', port=6379, db=0)

items = []

class Item(Resource):
    def get(self, name):
        result = r.lrange(name, 0, -1)

        if result:
            prices = []
            for x in result:
                prices.append(x.decode("utf-8"))
            return {'name': name, 'prices': prices}
        else:
            return {'item': None}, 404

    def post(self, name):
        data = request.get_json()
        item = {'name': name, 'prices': data['prices']}
        for x in data['prices']:
            r.lpush(name, int(x))
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
