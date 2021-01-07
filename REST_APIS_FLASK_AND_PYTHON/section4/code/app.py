from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from redis import Redis

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)
r = Redis(host='localhost', port=6379, db=0)


jwt = JWT(app, authenticate, identity)  # /auth

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, name):

        #for item in items:
        #    if item['name'] == name:
        #        return item
    #    return {'item': None}, 404

        #import ipdb;ipdb.set_trace()
        result = r.get(name)


        if result:
            #print("logs: get : with result", result)
            return {'name': str(name), 'price': result.decode("utf-8")}
        else:
            #print("logs: get : with none", result)
            return {'item': None}, 404

        #item = next(filter(lambda x: x['name'] == name, items), None)
        #return {'item': item}, 200 if item else 404

    def post(self, name):
        #if next(filter(lambda x: x['name'] == name, items), None):
        #    return {'message': "An item with name '{}' already exists.".format(name)}, 400
        #data = request.get_json()

        #item = {'name': name, 'price': 12.00}

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        r.set(name, data['price'])
        #print("logs: post: ", r)
        #items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        #print(data['another'])
        #data = request.get_json()
        chk = 0
        for item in items:
            if item['name'] == name:
                item.update(data)
                chk=1

        if chk == 0:
            item = {'name': name, 'price': data['price']}
            items.append(item)

        return item

        """
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item
        """


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
