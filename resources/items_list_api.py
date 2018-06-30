# =============================================================================
# This is items list api
# =============================================================================
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from models.item import ItemModel

class ItemList(Resource):

    @jwt_required
    def get(self):
        return {'items': [item.json() for item in ItemModel.find_all()]}

#----------------------------------------------------