# =============================================================================
# This is the items api
# =============================================================================

from flask_restful import Resource, reqparse
from flask_jwt_extended import (
        jwt_required, get_jwt_claims, fresh_jwt_required)

from models.item import ItemModel

class Item(Resource):

    # we want to get the price from the payload:
    parse = reqparse.RequestParser()
    parse.add_argument('price',
                       type=float,
                       required = True,
                       help = 'This field cannot be left blank!'
                       )

    parse.add_argument('store_id',
                       type=float,
                       required = True,
                       help = 'Every item requres store id!'
                       )

    @jwt_required
    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        return {'message': 'Item {} not found'.format(name)}, 404

    @fresh_jwt_required
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "Item with name '{}' already exists".format(name)}, 400

        data = Item.parse.parse_args()
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500

        return item.json(), 201 # tell the user it is created

    @jwt_required
    def delete(self, name):
        claims = get_jwt_claims()

        if not claims['is_admin']:
            return {'message': "Admin prevelige is needed!"}, 401

        try:
            item = ItemModel.find_by_name(name)

            if item:
                item.delete_from_db()
        except:
            return {'message': 'An error occurred deleting the item'}, 500

        return {'message': '{} deleted'.format(name)}

    @jwt_required
    def put(self, name):
        data = Item.parse.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
           item = ItemModel(name, **data)
        else:
           item.price = data['price']

        item.save_to_db()
        return item.json()
#----------------------------------------------------