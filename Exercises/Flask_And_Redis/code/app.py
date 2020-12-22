from flask import Flask
from flask_restful import Resource, Api, reqparse
from redis import Redis

app = Flask(__name__)
api = Api(app)
r = Redis(host='localhost', port=6379, db=0)


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, name):
        result = r.get(name)

        if result:
            return {'name': name, 'price': result.decode("utf-8")}
        else:
            return {'message': "Item is not found"}, 404

    def post(self, name):
        if r.get(name):
            return {'message': "An item with name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        r.set(name, data['price'])
        return item, 201

    def delete(self, name):
        result = r.delete(name)
        if result:
            return {'message': "Item deleted successfully"}, 201

        return {'message': "Item does not exist"}, 400

    def put(self, name):
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        r.set(name, data['price'])
        return item, 201


class ItemList(Resource):
    def get(self):
        items = []

        for key in r.scan_iter():
            items.append({'name': key.decode("utf-8"), 'price': r.get(key).decode("utf-8")})

        if items:
            return {'items': items}
        else:
            return {'message': "No items are found"}, 404


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000)
